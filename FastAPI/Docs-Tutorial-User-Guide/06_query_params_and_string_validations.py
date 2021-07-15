"""https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
How to pass a list of query params
validate query params nicely with Query
"""
# Builtins
from typing import List, Optional

# Third party
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    question: Optional[str] = Query(
        None, min_length=3, max_length=50, regex=r"[A-Za-z]*[?]$"
    ),
    # https://docs.python.org/3/library/constants.html#Ellipsis
    requeired_query: str = Query(..., min_length=3),
):
    """Demonstrates use of Query - even though
    question is optional it has to be max 50 in length
    minimum 3 in length
    has to be a question with ? at the end
    this ... stuff is called Ellipsis it make query required
    """
    results = {
        "items": [{"item_id": "Foo"}, {"item_id": "Bar"}],
        "requeired_query": requeired_query,
    }
    if question:
        results.update({"question": question})
    return results


@app.get("/items/list/")
async def read_filename_list(
    filenames: Optional[List[str]] = Query(
        ["cat.jpg", "dog.png"],
        regex=r"[a-zA-Z0-9]*\.(jpg|png|jpeg)$",
        description="Filenames for GCP signed urls generation",
        title="Filenames",
        alias="file-names",
    ),
    file: Optional[str] = Query("cat.png", deprecated=True),  # noqa W0613
):
    """How to pass a list of filenames
    example modified for utilization of previous experiences"""
    query_items = {"filenames": filenames}
    return query_items
