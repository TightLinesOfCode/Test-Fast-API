from fastapi import FastAPI

from api.config import Config
from api.Polygon import views as polygon_views
from api.Polygon.data import get_polygon_data

from api.Polygon.Alpaca import get_alpaca_data
from api.Polygon.Alpaca import ALPACADATA

app = FastAPI()
app.include_router(polygon_views.router, prefix="/Polygon")
config = Config()
print(config.dict())


@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/Account")
def account():
    return{"results": ALPACADATA[0]}


@app.on_event("startup")
async def startup_events():
    await get_polygon_data(config.POLYGON_REPOSITORY_URL)
    await get_alpaca_data()


# @app.on_event("startup")

