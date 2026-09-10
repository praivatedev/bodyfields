from typing import  Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI

class Item(BaseModel):
    name: str
    description: str | None = Field(default = None, title = "The description of the item", maxlength = 3000)
    price:  float = Field(gt = 0, description = "The price must be greater than zero")
    tax: float | None

@app.put("/item/{item_id}")
async def update_item(item_id: str, item: Annotated[Item, Body(embeded = true)]):
    results = {"item_id": item_id, "item": item}
    return results
