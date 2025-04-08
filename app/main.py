from fastapi import FastAPI
from .database import engine, Base
# from .routers import ... # If you organize routes into separate files

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World from FastAPI!"}

# Include routers here:
# app.include_router(your_router)