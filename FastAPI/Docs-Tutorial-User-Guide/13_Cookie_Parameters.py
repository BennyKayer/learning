"""https://fastapi.tiangolo.com/tutorial/cookie-params/
"""
# Builtins
from typing import Optional

# Third party
from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    """Demonstrates use of cookie params"""
    return {"ads_id": ads_id}
