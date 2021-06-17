"""Simplest api example with get presentation,
page shows generated docs in both swagger and redoc,
as well as other methods POST, PUT, PATCH, OPTIONS etc.
https://fastapi.tiangolo.com/tutorial/first-steps/#first-steps
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Basic api example"""
    return {"message": "Hello World"}
