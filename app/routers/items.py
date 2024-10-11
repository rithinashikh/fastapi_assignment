from fastapi import APIRouter
from app.models import ItemModel
from app.crud import (
    create_item, get_item_by_id, filter_items, aggregate_items,
    update_item_by_id, delete_item_by_id
)

router = APIRouter()

@router.post("/")
async def create_item_endpoint(item: ItemModel):
    return await create_item(item)

@router.get("/{id}")
async def get_item_by_id_endpoint(id: str):
    return await get_item_by_id(id)

@router.get("/filter")
async def filter_items_endpoint(
    email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None
):
    return await filter_items(email, expiry_date, insert_date, quantity)

@router.get("/aggregate")
async def aggregate_items_endpoint():
    return await aggregate_items()

@router.put("/{id}")
async def update_item_endpoint(id: str, item: ItemModel):
    return await update_item_by_id(id, item)

@router.delete("/{id}")
async def delete_item_endpoint(id: str):
    return await delete_item_by_id(id)
