from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


app = FastAPI(title="E2E Test API", version="1.0.0")

items_db = []


@app.get("/")
def read_root():
    return {"message": "E2E Test API", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "items_count": len(items_db)}


@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    item_dict["id"] = len(items_db) + 1
    items_db.append(item_dict)
    return {"item": item_dict, "message": "Item created successfully"}


@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"items": items_db[skip : skip + limit], "total": len(items_db)}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return {"item": item}
    return {"error": "Item not found"}
