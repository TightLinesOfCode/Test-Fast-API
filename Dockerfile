# Multi-stage build to reduce image size
# See https://pythonspeed.com/articles/multi-stage-docker-python/
FROM python:3.8.6-slim as py

# Base
FROM py as base
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential python-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY api ./api/
COPY setup.py ./

# Dev
FROM base as develop
COPY --from=base / /
COPY start.dev.sh ./

RUN pip3 install --no-cache-dir -e .

EXPOSE 8000


ENTRYPOINT ["uvicorn"]

# Production
# TODO