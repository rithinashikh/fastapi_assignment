
from fastapi import FastAPI
from app.routers import items, clock_in

app = FastAPI()


app.include_router(items.router, prefix="/items", tags=["Items"])
app.include_router(clock_in.router, prefix="/clock-in", tags=["Clock-In Records"])
