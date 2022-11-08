from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/train/{user_id}/{item_id}")
def train(user_id: str, item_id: int):
    
    return {"user_id": user_id, "item_id": item_id}