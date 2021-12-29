"""https://fastapi.tiangolo.com/tutorial/response-model/
"""
# Builtins
from typing import List, Optional

# Third party
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    """Will be used as response_model"""

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []


@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    """Demonstrates response_model param
    FastAPI will use this response_model to:

    Convert the output data to its type declaration.
    Validate the data.
    Add a JSON Schema for the response, in the OpenAPI path operation.
    Will be used by the automatic documentation systems.
    Will limit the output data to that of the model.
    """
    return item


class UserIn(BaseModel):
    """Stuff required for user
    request data
    """

    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    """Stuff returned for user
    response data
    """

    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    """Demonstrates the use case for response model
    with user creation we want password in request
    but not in response
    """
    return user


class DefaultItem(BaseModel):
    """Item with a lots of defaults
    to demonstrate response_model_exclude_unset
    """

    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {
        "name": "Bar",
        "description": "The bartenders",
        "price": 62,
        "tax": 20.2,
    },
    "baz": {
        "name": "Baz",
        "description": None,
        "price": 50.2,
        "tax": 10.5,
        "tags": [],
    },
}


@app.get(
    "/items_def/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
)
async def read_items(item_id: str):
    """response_model_exclude_unset will case endpoint
    to only return stuff that has been set instead of long list of defaults
    it's supposedely helpfull in NoSql databases
    """
    return items[item_id]


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
    # Can be ["name", "description"]
)
async def read_item_name(item_id: str):
    """Demonstrates response_model_include"""
    return items[item_id]


@app.get(
    "/items/{item_id}/public",
    response_model=Item,
    response_model_exclude={"tax"},
    # Can be ["name", "description"]
)
async def read_item_public_data(item_id: str):
    """Demonstrates response_model_exclude"""
    return items[item_id]
