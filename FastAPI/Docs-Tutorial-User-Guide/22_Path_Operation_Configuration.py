"""Path operation configuration, shows this cool thing with description
"""
# Builtins
from typing import Optional, Set

# Third party
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["item"],
)
async def create_item(item: Item):
    """Status codes demo, just like in django"""
    return item


# tags are those "groups" in swagger like endpoints under items/ or users/ etc.
# deprecation does this strike through thing in the docs
@app.get("/users/", tags=["users"], deprecated=True)
async def get_users():
    return [{"username": "johndoe"}]


# description parameter can be replaced by endpoint's docstring!
# response_description is this stuff below that says "Successful response"
# summary is this string that shows up on the right of the endpoint button
@app.get(
    "/items/",
    tags=["items"],
    summary="Get list of items",
    response_description="List of items",
)
async def read_items():
    """Get all items from the database
    item consists of:

    - **name**: Display name of an item
    - **description**: Long description of an item
    - **price**: Price of an item
    - **tax**: Optional tax on an item (some items are exempted from taxation like gasoline should be)
    - **tags**: Set of categories to which an item falls into
    """
    return [{"name": "Foo", "price": 42}]
