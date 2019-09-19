from fastapi import FastAPI
from pydantic import BaseModel
from typing import Iterable

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
async def read_root() -> Item:
    return Item(name="3434", price=3.3, is_offer=True)
    # return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> Iterable[Item]:
    return {
        "item_name": item.name,
        "item_id": item_id
    }
