"""
https://fastapi.tiangolo.com/tutorial/extra-models/
"""
# Builtins
from typing import List, Optional, Union

# Third party
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    """[summary]"""

    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    """[summary]"""

    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserInDb(BaseModel):
    """[summary]"""

    username: str
    hashed_password: str
    email: EmailStr
    full_name: Optional[str] = None


def fake_password_hasher(raw_password: str):
    """[summary]

    Args:
        raw_password (str): [description]

    Returns:
        [type]: [description]
    """
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    """[summary]

    Args:
        user_in (UserIn): [description]

    Returns:
        [type]: [description]
    """
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDb(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ...not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    """[summary]

    Args:
        user_in (UserIn): [description]

    Returns:
        [type]: [description]
    """
    user_saved = fake_save_user(user_in)
    return user_saved


# This 3 models need to be in sync ...
# this is a maintenance headache
# soo....


class UserBase(BaseModel):
    """[summary]"""

    username: str
    email: EmailStr
    full_name: Optional[str] = None


class BetterUserIn(UserBase):
    """[summary]"""

    password: str


class BetterUserOut(UserBase):
    """[summary]"""


class BetterUserInDb(UserBase):
    """[summary]"""

    hashed_password: str


# Now onto the Union - returning one of two models


class BaseItem(BaseModel):
    """[summary]"""

    description: str
    type: str


class CarItem(BaseItem):
    """[summary]"""

    type = "car"


class PlaneItem(BaseItem):
    """[summary]"""

    type = "plane"
    size: int


items = {
    "item1": {
        "description": "All my friends drive a low rider",
        "type": "car",
    },
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    """[summary]

    Args:
        item_id (str): [description]

    Returns:
        [type]: [description]
    """
    return items[item_id]


# With same spirit return list of objects
@app.get("/items/", response_model=List[BaseItem])
async def read_items():
    """[summary]

    Returns:
        [type]: [description]
    """
    return items
