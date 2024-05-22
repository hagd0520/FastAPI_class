from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    

def get_item_from_db(id):
    # 매우 간단한 아이템 반환
    return {
        "name": "Simple Item",
        "description": "A simple item description",
        "price": 50.0,
        "dis_pirce": 45.0
    }
    
    
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    item = get_item_from_db(item_id)
    return item


class Cat(BaseModel):
    name: str
    
    
class Dog(BaseModel):
    name: str
    
    
@app.get("/animal", response_model=Cat)
async def get_animal(animal: str):
    if animal == "cat":
        return Dog(name="Whiskers")
    else:
        return Dog(name="Fido")
    
    
class Item2(BaseModel):
    name: str
    
    
@app.get("/items", response_model=List[Item2])
async def get_items():
    return [{"name": "Item 1"}, {"name": "Item 2"}]