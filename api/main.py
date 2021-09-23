from fastapi import FastAPI

from api.Polygon import views as  polygon_views

app = FastAPI()
app.include_router(polygon_views.router, prefix="/polygon")
@app.get("/health")
def health():
    return {"status":"ok"}

