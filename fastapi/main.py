from typing import Union
import api

from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()


class Item(BaseModel):
    rss: str



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post('/transcribe')
def my_function(item: Item):
    transcript = api.run()
    return transcript

# @app.post('/summarize')
# def my_function(rss: str):
#     print("summarize")

