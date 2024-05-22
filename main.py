from typing import Dict, List
from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# @app.get("/items")
# def read_items(skip = 0, limit = 10):
#     return {"skip": skip, "limit": limit}


# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}


@app.get("/items")
async def read_items(q: List[int] = Query([])):
    return {"q": q}


@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item


@app.get("/getdata")
def read_items(data: str = "funcoding"):
    return {"data": data}