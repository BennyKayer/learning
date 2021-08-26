"""https://fastapi.tiangolo.com/tutorial/request-forms/
"""
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    """Example of using Form parameters (same as Body and Query)
    Cannot use in conjunction with Body (well it makes sense)
    """
    if password:
        return {"username": username}
    return {"error": "error"}
