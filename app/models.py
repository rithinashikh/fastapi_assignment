
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ItemModel(BaseModel):
    name: str
    description: Optional[str]
    price: float
    quantity: int
    expiry_date: Optional[datetime]
    insert_date: Optional[datetime]
    email: Optional[str]

class ClockInModel(BaseModel):
    employee_id: str
    location: Optional[str]
    insert_datetime: datetime
    email: Optional[str]
