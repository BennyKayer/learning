"""https://fastapi.tiangolo.com/tutorial/response-status-code/
"""

from fastapi import FastAPI, status

app = FastAPI()


@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    """Shows how to declare successful status code"""
    return {"name": name}
