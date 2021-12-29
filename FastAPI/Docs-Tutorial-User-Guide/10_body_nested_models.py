"""https://fastapi.tiangolo.com/tutorial/body-nested-models/
"""
# Builtins
from typing import Dict, List, Optional, Set

# Third party
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    """Submodel for nesting demonstration"""

    url: HttpUrl
    name: str


class Item(BaseModel):
    """Item for nesting example"""

    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    """Deep nesting example model"""

    name: str
    description: Optional[str]
    price: float
    items: List[Item]


@app.post("/offers/")
async def create_offer(offer: Offer):
    """Create offer"""
    return offer


@app.post("/offers/many/")
async def create_many_offers(offers: List[Offer]):
    """Create many offers"""
    return offers


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """Endpoint for nesting demonstration"""
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/index_weights/")
async def create_index_weights(weights: Dict[int, float]):
    """Demonstrates that although JSON only sends string
    validation of data to be int and float is performed
    """
    return weights
