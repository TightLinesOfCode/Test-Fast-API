from fastapi import APIRouter

from api.Polygon.data import POLYGONDATA
from api.Polygon.Alpaca import ALPACADATA


router = APIRouter()




@router.get("/Account")
def account():
    return {"results": ALPACADATA[0]}
