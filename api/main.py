from fastapi import FastAPI

from api.config import Config
from api.Polygon import views as polygon_views
from api.Polygon.data import get_polygon_data

app = FastAPI()
app.include_router(polygon_views.router, prefix="/polygon")
config = Config()
print(config.dict())

@app.get("/health")
def health():
    return{"status": "ok"}


@app.on_event("startup")
async def load_polygon_data():
    #await get_polygon_data(config.polygon_test_url)
    get_polygon_data(config.polygon_test_url)
