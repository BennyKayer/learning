"""Entry point for every FastAPI application
can be name whatever
"""
from typing import List, Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

###############################################################################
# https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters
# If you don't want to add a specific value but just make it optional, set the default as None.
# But when you want to make a query parameter required, you can just not declare any default value:


@app.get("/items/required/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


# https://fastapi.tiangolo.com/tutorial/query-params/#required-query-parameters
###############################################################################


########################################################################################
# https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters


@app.get("users/{user_id}/items/{item_id}")
async def read_user_item_multi_query(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "This is an amazing item that has a long description"
            }
        )
    return item


# https://fastapi.tiangolo.com/tutorial/query-params/#multiple-path-and-query-parameters
########################################################################################


#########################################################################
# https://fastapi.tiangolo.com/tutorial/query-params/#optional-parameters


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
