from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None) \
        -> dict[str, str | None]:
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item) -> dict[str, int | Item]:
    return {"item_id": item_id, "item": item}
