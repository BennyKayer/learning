"""https://fastapi.tiangolo.com/tutorial/body-multiple-params/
Showing mixing of Query, Path and Body params with all the previous validations
"""
from typing import Optional

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel  # noqa E0611

app = FastAPI()


class Item(BaseModel):
    """Item"""

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    """User"""

    name: str
    fullname: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(
        ..., title="The ID of the item to update", ge=0, le=1000
    ),
    # not present in path => query param
    query: Optional[str] = None,
    # All that inherits from Pydantic Base model will be treated as body
    # this will expect keys name desc price etc in request body
    item: Optional[Item] = None,
    # this will embed inside item key
    item_embed: Item = Body(..., embed=True),
    user: Optional[User] = None,
    # without Body FastAPI treats single values as query params
    importance: int = Body(..., gt=0)
):
    """Presents mixture of Path, Query and body params

    Args:
        item_id (int, optional): Path param.
        Defaults to
        Path(..., title="The ID of the item to update", ge=0, le=1000).
        query (Optional[str], optional): Query param. Defaults to None.
        item (Optional[Item], optional): Body param. Defaults to None.
    """
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "query": query,
        "importance": importance,
        "item_embed": item_embed,
    }
    return results
