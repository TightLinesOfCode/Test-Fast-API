from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_data():
    return {"working polygon":"need data"}