from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI


class Item(BaseModel):
    name: str
    description: str | None = None    #默认值为 None 的模型属性也是可选的
    price: float
    tax: float | None = None


app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q} 

@app.put("/items/{item_id}")
async def update_item(item_id:int, item: Item):
    return {"item_id": item_id, **item.dict()}

@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == '__main__' :
    uvicorn.run(app='main:app', host="127.0.0.1", port= 8000, reload= True)