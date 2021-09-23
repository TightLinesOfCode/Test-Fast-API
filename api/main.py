from fastapi import FastAPI

from api.Polygon import views as  polygon_views

app = FastAPI()
app.inclue_router(polygon_views.router, prefix="/polygon")
@app.get("/health")
def health():
    return {"status":"ok"}

