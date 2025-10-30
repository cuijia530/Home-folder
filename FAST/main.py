from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def get_users():
    return {"hello":'messages'}

@app.get('/items')
async def read_items(q: str | None = None):
    return { }



@app.get('/items/me')
async def get_items_me():
    return {"user": f'这是一个没有路径的数据'}

@app.get('/items/{items_id}')
async def get_items(items_id:int):
    return {'items': items_id}

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port= 8000, reload=True,)