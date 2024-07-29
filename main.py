from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None) \
        -> dict[str, str | None]:
    return {"item_id": item_id, "q": q}
