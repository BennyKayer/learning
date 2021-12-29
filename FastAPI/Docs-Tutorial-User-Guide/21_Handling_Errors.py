"""https://fastapi.tiangolo.com/tutorial/handling-errors/
"""
# Third party
from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND  # HTTP_400_BAD_REQUEST,
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


class UnicornException(Exception):
    """Custom exception to demonstrate global exception handler"""

    def __init__(self, name: str):
        super().__init__()
        self.name = name


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(
#     request: Request, exc: RequestValidationError
# ):
#     """Override the Validation Error presentation"""
#     return PlainTextResponse(str(exc), status_code=HTTP_400_BAD_REQUEST)


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """Handle custom exception"""
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Opps! {exc.name} did something. There goes a rainbow"
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    """Can be used while developing to get more error details"""
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    """Demonstrates the usage of HTTPException"""
    if item_id not in items:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail="Item not found",
            headers={"X-Error": "There goes my error"},
        )
    if item_id == "yolo":
        raise UnicornException(name=item_id)
    return {"item": items[item_id]}
