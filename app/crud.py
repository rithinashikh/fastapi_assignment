from bson import ObjectId
from app.database import items_collection, clock_in_collection
from app.models import ItemModel, ClockInModel
from fastapi import HTTPException
from datetime import datetime
import logging

async def create_item(item: ItemModel):
    new_item = await items_collection.insert_one(item.dict())
    return str(new_item.inserted_id)

def serialize_mongo_object(obj):
    if "_id" in obj:
        obj["_id"] = str(obj["_id"]) 
    return obj

async def filter_items(email=None, expiry_date=None, insert_date=None, quantity=None):
    try:
        query = {}
        if email:
            query['email'] = email  
        if expiry_date:
            query['expiry_date'] = {"$gte": datetime.strptime(expiry_date, "%Y-%m-%d")}  
        if insert_date:
            query['insert_date'] = {"$gte": datetime.strptime(insert_date, "%Y-%m-%d")}  
        if quantity is not None:
            query['quantity'] = {"$gte": quantity}  
        
        logging.info(f"Generated query: {query}")  
        
        items = await items_collection.find(query).to_list(100)  
        return [serialize_mongo_object(item) for item in items]  
    except Exception as e:
        logging.error(f"Error in filter_items: {str(e)}")  
        raise HTTPException(status_code=500, detail="Internal Server Error") 

async def get_item_by_id(id: str):
    try:
        if not ObjectId.is_valid(id):
            raise HTTPException(status_code=400, detail="Invalid ID format")
        item = await items_collection.find_one({"_id": ObjectId(id)})
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return serialize_mongo_object(item) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def aggregate_items():
    try:
        print("inside aggregate")
        pipeline = [
            {
                "$group": {
                    "_id": "$email",              
                    "total_items": {"$sum": 1}   
                }
            }
        ]
        result = await items_collection.aggregate(pipeline).to_list(100)
        logging.info(f"Aggregation Result: {result}")  
        return result
    except Exception as e:
        logging.error(f"Error in aggregation: {str(e)}")  
        raise HTTPException(status_code=500, detail=str(e))


async def update_item_by_id(id: str, item: ItemModel):
    updated_item = await items_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": item.dict(exclude={"insert_date"})}
    )
    return updated_item.modified_count

async def delete_item_by_id(id: str):
    result = await items_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count

async def create_clock_in(clock_in: ClockInModel):
    new_clock_in = await clock_in_collection.insert_one(clock_in.dict())
    return str(new_clock_in.inserted_id)

async def get_clock_in_by_id(id: str):
    try:
        clock_in = await clock_in_collection.find_one({"_id": ObjectId(id)})
        if clock_in:
            return serialize_mongo_object(clock_in) 
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def filter_clock_in(email=None, location=None, insert_datetime=None):
    query = {}
    if email:
        query['email'] = email
    if location:
        query['location'] = location
    if insert_datetime:
        query['insert_datetime'] = {"$gte": datetime.strptime(insert_datetime, "%Y-%m-%d")}
    clock_ins = await clock_in_collection.find(query).to_list(100)
    return clock_ins

async def update_clock_in_by_id(id: str, clock_in: ClockInModel):
    updated_clock_in = await clock_in_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": clock_in.dict(exclude={"insert_datetime"})}
    )
    return updated_clock_in.modified_count

async def delete_clock_in_by_id(id: str):
    result = await clock_in_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count
