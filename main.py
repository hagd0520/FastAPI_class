from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    is_offer: bool = None
    

@app.post("/items")
def create_item(item: Item):
    return {"item": item.model_dump()}