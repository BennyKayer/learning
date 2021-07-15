"""
This one has refs to some of the examples props
https://fastapi.tiangolo.com/tutorial/schema-extra-example/
"""

# Builtins
from typing import Optional

# Third party
from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel, Field  # noqa E0611

app = FastAPI()


class Item(BaseModel):
    """This time demonstrates use of Config Subclass
    schema_extra has some kind of example
    all of the
    Path(),Query(),Header(),Cookie(),Body(),Form(),File()
    can also get example in param
    """

    # 2nd way
    name: str = Field(..., example="foo")
    description: Optional[str] = Field(None, example="Nice item it is hmmm")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)

    class Config:
        """Class used to define extra stuff for openAPI etc."""

        # 1st way
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    # 3rd way
    item: Item = Body(
        ...,
        example={
            "name": "Foo",
            "description": "Bar",
            "price": 35.3,
            "tax": 3.2,
        },
    ),
):
    """example in body is a 3rd way to show example in OpenApi"""
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items_many_examples/{item_id}")
async def update_item_many_examples(
    *,
    item_id: int,
    item: Item = Body(
        ...,
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "Normal item works correctly",
                "value": {
                    "name": "Foo",
                    "description": "a very nice item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",  # noqa E501
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    )
):
    """Demonstrates many examples usage"""
    results = {"item_id": item_id, "item": item}
    return results
