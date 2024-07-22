from typing import Union

from fastapi import FastAPI

app = FastAPI(root_path="/test")


@app.get("/")
def read_root():
    return {"Hello": "World"}