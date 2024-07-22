from typing import Union
from fastapi import FastAPI, Request

app = FastAPI(root_path="/test")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/request")
async def read_request(request: Request):
    body = None
    if request.headers.get("content-type") and request.headers["content-type"] == "application/json":
        body = await request.json()
    return {
        "base_url" : request.base_url,
        "headers": request.headers,
        "receive":request.receive,
        "query_params": request.query_params,
        "body": body
    }