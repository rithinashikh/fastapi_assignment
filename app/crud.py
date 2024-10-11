# app/crud.py
from bson import ObjectId
from app.database import items_collection, clock_in_collection
from app.models import ItemModel, ClockInModel

# Helper functions for items collection
async def create_item(item: ItemModel):
    new_item = await items_collection.insert_one(item.dict())
    return str(new_item.inserted_id)

async def get_item_by_id(id: str):
    item = await items_collection.find_one({"_id": ObjectId(id)})
    if item:
        return item
    return None

async def filter_items(email=None, expiry_date=None, insert_date=None, quantity=None):
    query = {}
    if email: query['email'] = email
    if expiry_date: query['expiry_date'] = expiry_date
    if insert_date: query['insert_date'] = insert_date
    if quantity: query['quantity'] = quantity
    items = await items_collection.find(query).to_list(100)
    return items

async def aggregate_items():
    pipeline = [{"$group": {"_id": "$email", "total_items": {"$sum": "$quantity"}}}]
    result = await items_collection.aggregate(pipeline).to_list(100)
    return result

async def update_item_by_id(id: str, item: ItemModel):
    updated_item = await items_collection.update_one({"_id": ObjectId(id)}, {"$set": item.dict()})
    return updated_item.modified_count

async def delete_item_by_id(id: str):
    result = await items_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count

# Helper functions for clock_in collection
async def create_clock_in(clock_in: ClockInModel):
    new_clock_in = await clock_in_collection.insert_one(clock_in.dict())
    return str(new_clock_in.inserted_id)

async def get_clock_in_by_id(id: str):
    clock_in = await clock_in_collection.find_one({"_id": ObjectId(id)})
    if clock_in:
        return clock_in
    return None

async def filter_clock_in(email=None, location=None, insert_datetime=None):
    query = {}
    if email: query['email'] = email
    if location: query['location'] = location
    if insert_datetime: query['insert_datetime'] = insert_datetime
    clock_ins = await clock_in_collection.find(query).to_list(100)
    return clock_ins

async def update_clock_in_by_id(id: str, clock_in: ClockInModel):
    updated_clock_in = await clock_in_collection.update_one({"_id": ObjectId(id)}, {"$set": clock_in.dict()})
    return updated_clock_in.modified_count

async def delete_clock_in_by_id(id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count
