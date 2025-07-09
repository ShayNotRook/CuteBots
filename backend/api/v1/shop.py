from fastapi import APIRouter



router = APIRouter(prefix="/shop")


@router.get("/items/")
async def get_home_items():
    pass