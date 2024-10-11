
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_DETAILS

client = AsyncIOMotorClient(MONGO_DETAILS)

database = client.myDatabase
items_collection = database.get_collection("items")
clock_in_collection = database.get_collection("clock_in")
