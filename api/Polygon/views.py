from fastapi import APIRouter

from api.Polygon.data import POLYGONDATA



router = APIRouter()

@router.get("")
def list_data():
    return {"results": POLYGONDATA[0]}


# @router.get("/Account")
# def account():
#    return {"results": ALPACADATA[0]}
