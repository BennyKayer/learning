"""https://fastapi.tiangolo.com/tutorial/cookie-params/
"""
from typing import Optional
from fastapi import FastAPI, Cookie

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    """Demonstrates use of cookie params"""
    return {"ads_id": ads_id}
