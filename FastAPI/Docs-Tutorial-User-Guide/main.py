"""Entry point for every FastAPI application
can be name whatever
"""
# Builtins
from enum import Enum
from typing import List, Optional

# Third party
from fastapi import FastAPI
from pydantic import BaseModel


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
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item


@app.get("/items_optional/{item_id}")
async def read_item_optional(item_id: str, q: Optional[str] = None):
    res = {"item_id": item_id, "q": q} if q else {"item_id": item_id}
    return res


@app.get("/items_short/{item_id}")
async def read_item_short(
    item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        dsc = "This is an amazing item that has a long description"
        item.update({"description": dsc})
    return item


# https://fastapi.tiangolo.com/tutorial/query-params/#optional-parameters
#########################################################################


######################################################################
# https://fastapi.tiangolo.com/tutorial/query-params/#query-parameters

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items/")
async def read_item_paging(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/filenames/")
async def get_file_names(filenames: List[str]):
    return filenames


# https://fastapi.tiangolo.com/tutorial/query-params/#query-parameters
######################################################################


#####################################################################################
# https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-containing-paths


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters-containing-paths
#####################################################################################

#####################################################################################
# https://fastapi.tiangolo.com/tutorial/path-params/#working-with-python-enumerations
class ModelName(str, Enum):
    """Only accept this values"""

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    message = ""
    # can also do model_name == 'alexnet' etc.
    if model_name == ModelName.alexnet:
        message = "Deep Learning FTW!"
    if model_name == ModelName.lenet:
        message = "LeCNN all the images"
    if model_name == ModelName.resnet:
        message = "Have some residuals"

    return {"model_name": model_name, "message": message}


# https://fastapi.tiangolo.com/tutorial/path-params/#working-with-python-enumerations
#####################################################################################

##################################################################
# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters


@app.get("/users/me")
async def read_user_me():
    """Must be before /users/{user_id} in order to work"""
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """Otherwise it'll think that it receives "me" as user_id"""
    return {"user_id": user_id}


# https://fastapi.tiangolo.com/tutorial/path-params/#order-matters
##################################################################


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
