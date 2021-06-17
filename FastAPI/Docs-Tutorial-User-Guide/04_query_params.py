"""Section for query parameters
https://fastapi.tiangolo.com/tutorial/query-params/
"""
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items/")
async def read_item_paging(skip: int = 0, limit: int = 10):
    """Shows that if provided defaults query params will be optional"""
    return fake_items_db[skip : skip + limit]


@app.get("/items_optional/{item_id}")
async def read_item_optional(item_id: str, question: Optional[str] = None):
    """Other way to make optional query params - more explicit one"""
    res = (
        {"item_id": item_id, "q": question}
        if question
        else {"item_id": item_id}
    )
    return res


@app.get("/items_short/{item_id}")
async def read_item_short(
    item_id: str, q: Optional[str] = None, short: bool = False
):
    """Optional query params with bool converter"""
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        dsc = "This is an amazing item that has a long description"
        item.update({"description": dsc})
    return item


@app.get("users/{user_id}/items/{item_id}")
async def read_user_item_multi_query(
    user_id: int,
    item_id: str,
    question: Optional[str] = None,
    short: bool = False,
):
    """Demonstrates the mixture of path and query parameters
    https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters
    """
    item = {"item_id": item_id, "owner_id": user_id}
    if question:
        item.update({"q": question})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long desc"}
        )
    return item


@app.get("/items/required/{item_id}")
async def read_user_item(item_id: str, needy: str):
    """
    https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters
    If you don't want to add a specific value but just make it optional,
    set the default as None.
    But when you want to make a query parameter required,
    you can just not declare any default value:
    """
    item = {"item_id": item_id, "needy": needy}
    return item
