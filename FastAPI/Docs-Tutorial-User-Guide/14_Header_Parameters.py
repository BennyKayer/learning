"""https://fastapi.tiangolo.com/tutorial/header-params/
"""
# Builtins
from typing import List, Optional

# Third party
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
    weird_header: Optional[str] = Header(None, convert_underscores=False),
):
    """Demonstrates usage of header params
    User-Agent gets automatically converted to python variable user_agent
    thus can be read here
    weird header is weird and does not convert underscores to -
    so the HTTP proxies will block him
    """
    return {"User-Agent": user_agent, "weird": weird_header}


@app.get("/x_token/")
async def x_token_end(x_token: Optional[List[str]] = Header(None)):
    """Demonstrates list usage for headers that may appear many times"""
    return {"X-Token values": x_token}
