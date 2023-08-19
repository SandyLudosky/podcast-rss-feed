from fastapi import FastAPI, Body,  HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.security import APIKeyHeader

import os
import api

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

origins = ["*"]

api_keys = [
    os.getenv("OPENAI_API_KEY")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_api_key(api_key_header: str = Security(api_key_header)) -> str:
    if api_key_header in api_keys:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )


class Item(BaseModel):
    rss: str


class Transcript(BaseModel):
    content: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/protected")
def protected_route(api_key: str = Security(get_api_key)):
    # Process the request for authenticated users
    return {"message": "Access granted!"}


@app.post('/transcribe')
def transcribe(item: Item):
    result = api.runAPI(item.rss)
    print(result)
    return result


@app.post('/summarize')
def summarize(transcript: Transcript):
    summary = api.run(transcript.content)
    return summary
