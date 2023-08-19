from typing import Union
import api

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    rss: str


class Transcript(BaseModel):
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/transcribe')
def transcribe(item: Item):
    transcript = api.run(item.rss)
    return transcript


@app.post('/summarize')
def summarize(transcript: Transcript):
    summary = api.run(transcript.content)
    return summary

# @app.post('/summarize')
# def my_function(rss: str):
#     print("summarize")
