from typing import Any

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/pubsub")
async def pubsub(data: dict) -> Any:
    print(data)
    return data
