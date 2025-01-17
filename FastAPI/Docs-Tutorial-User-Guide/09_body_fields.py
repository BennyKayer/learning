"""https://fastapi.tiangolo.com/tutorial/body-fields/
"""

# Builtins
from typing import Optional

# Third party
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    """Item with Field Usage"""

    name: str
    description: Optional[str] = Field(
        None, title="The description of the item", max_length=300
    )
    price: float = Field(
        ..., gt=0, description="The price must be greater than zero"
    )
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    """Endoint that uses Item with Field usage"""
    results = {"item_id": item_id, "item": item}
    return results
