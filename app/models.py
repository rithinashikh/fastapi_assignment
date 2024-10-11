from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ItemModel(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: Optional[datetime]
    insert_date: Optional[datetime] = Field(default_factory=datetime.utcnow)

class ClockInModel(BaseModel):
    email: str
    location: Optional[str] = None
    insert_datetime: Optional[datetime] = Field(default_factory=datetime.utcnow)
