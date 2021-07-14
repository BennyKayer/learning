"""https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
    Query and Path both inherit from Param class so they have same params
"""
from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(..., title="The ID of the item to get"),
    query: Optional[str] = Query(None, alias="item-query"),
):
    """Demonstrated Path that takes the same params as Query,
    Path is always required so ... makes sense while None does not
    """
    results = {
        "item_id": str(item_id),
    }
    if query:
        results.update({"query": query})
    return results


@app.get("/items_query_required/{item_id}")
async def read_items_query_req(
    q: str, item_id: int = Path(..., title="The ID of the item to get")
):
    """Scenario with required query, reordered so that python won't complain"""
    results = {
        "item_id": str(item_id),
    }
    if q:
        results.update({"q": q})
    return results


@app.get("/items_treat_all_as_kwargs/{item_id}")
async def read_items_all_kwargs(
    *, item_id: int = Path(..., title="The ID of the item to get"), query: str
):
    """Passing * first will inform Python
    "hey treat all params as kwargs"
    """
    results = {
        "item_id": str(item_id),
    }
    if query:
        results.update({"query": query})
    return results


@app.get("/items_numeric_validation_greater_than_equal/{item_id}")
async def read_items_greater_than_equal(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=1, le=1000),
    q: str,
    size: float = Query(..., gt=0, lt=10.5)
):
    """Passing numeric validation
    greater than or equal and
    less than or equal
    to the Path param
    and greater than and less than
    to the query param
    """
    results = {"item_id": str(item_id)}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": str(size)})
    return results
