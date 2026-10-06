from fastapi import FastAPI
from pydantic import BaseModel 

app = FastAPI()
class Item(BaseModel):
    name: str
    price: float

items={}

@app.post("/items/")
async def create_items(item: Item):
    item_id = len(items)+ 1
    items[item_id]= item
    return { 
        "id": item_id, 
        "item": item
    }

@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return items.get(item_id, { 
        "error": "Not Found Item"
    })

@app.put("/items/{item_id}")
async def update_items(item_id: int, item: Item): 
   if item_id in items: 
        items[item_id] = item
        return { "message": "Item is updated", "item" : item}


@app.delete("/items/{item_id}")
async def remove_items(item_id: int):
    if item_id in items: 
        deleted_item = items.pop(item_id)
        return {"message" : "Item removed", "item" : deleted_item}
    return {"error": "Item not found"}