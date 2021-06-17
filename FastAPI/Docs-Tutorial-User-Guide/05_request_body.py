"""https://fastapi.tiangolo.com/tutorial/body/
"""
# Builtins
from typing import Optional

# Third party
from fastapi import FastAPI
from pydantic import BaseModel  # noqa E0601


class Item(BaseModel):
    name: str
    description: Optional[str]
    price: float
    tax: Optional[float]


app = FastAPI()


@app.put("/items/{item_id}")
async def create_item_body_path_query_params(
    item_id: int, item: Item, question: Optional[str] = None
):
    """Demonstrates use of all request body, path and query parameters
    If the parameter is also declared in the path,
    it will be used as a path parameter.
    If the parameter is of a singular type (like int, float, str, bool, etc)
    it will be interpreted as a query parameter.
    If the parameter is declared to be of the type of a Pydantic model,
    it will be interpreted as a request body.

    Args:
        item_id (int): Query parameter
        item (Item): Request body
        question (Optional[str], optional): Path parameter. Defaults to None.

    Returns:
        [type]: [description]
    """
    result = {"item_id": item_id, **item.dict()}
    if question:
        result.update({"question": question})
    return result


@app.post("/items/{item_id}")
async def create_item_req_path(item_id: int, item: Item):
    """Version of create item
    that demonstarates that both request body and path params
    can be used at the same time"""
    return {"item_id": item_id, **item.dict()}


@app.post("/items/")
async def create_item(item: Item):
    """Demonstartes an endpoint with reqeust body"""
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
