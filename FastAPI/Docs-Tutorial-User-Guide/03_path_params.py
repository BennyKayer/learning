"""Tells about pydantic validation, path params, enums etc.
https://fastapi.tiangolo.com/tutorial/path-params/
"""
# Builtins
from enum import Enum

# Third party
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    """Path params"""
    return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item_type(item_id: int):
    """Path params with types"""
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    """Presented in conjuction with read_user,
    /me has to be first otherwise it'll
    be treated as user_id path param
    """
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """Presented in conjuction with read_user,
    /me has to be first otherwise it'll
    be treated as user_id path param
    """
    return {"user_id": user_id}


class ModelName(str, Enum):
    """Only accept this values
    used in get_model to present enums
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """Demonstrates how to use enums"""
    message = ""
    # can also do model_name == 'alexnet' etc.
    if model_name == ModelName.alexnet:
        message = "Deep Learning FTW!"
    if model_name == ModelName.lenet:
        message = "LeCNN all the images"
    if model_name == ModelName.resnet:
        message = "Have some residuals"

    return {"model_name": model_name, "message": message}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """Demonstrates how to use path convertor"""
    return {"file_path": file_path}
