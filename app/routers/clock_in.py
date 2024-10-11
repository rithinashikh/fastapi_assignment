from fastapi import APIRouter
from app.models import ClockInModel
from app.crud import (
    create_clock_in, get_clock_in_by_id, filter_clock_in,
    update_clock_in_by_id, delete_clock_in_by_id
)

router = APIRouter()

@router.post("/")
async def create_clock_in_endpoint(clock_in: ClockInModel):
    return await create_clock_in(clock_in)

@router.get("/{id}")
async def get_clock_in_by_id_endpoint(id: str):
    return await get_clock_in_by_id(id)

@router.get("/filter")
async def filter_clock_in_endpoint(email: str = None, location: str = None, insert_datetime: str = None):
    return await filter_clock_in(email, location, insert_datetime)

@router.put("/{id}")
async def update_clock_in_endpoint(id: str, clock_in: ClockInModel):
    return await update_clock_in_by_id(id, clock_in)

@router.delete("/{id}")
async def delete_clock_in_endpoint(id: str):
    return await delete_clock_in_by_id(id)
