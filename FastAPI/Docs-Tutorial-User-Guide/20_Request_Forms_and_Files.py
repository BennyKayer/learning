"""https://fastapi.tiangolo.com/tutorial/request-forms-and-files/
"""
# Third party
from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    small_file: bytes = File(...),
    big_file: UploadFile = File(...),
    token: str = Form(...),
):
    """Demonstrates use of both File and Form params

    Args:
        small_file (bytes, optional): [description]. Defaults to File(...).
        big_file (UploadFile, optional): [description]. Defaults to File(...).
        token (str, optional): [description]. Defaults to Form(...).

    Returns:
        [type]: [description]
    """
    return {
        "small_file_size": len(small_file),
        "token": token,
        "big_file_content_type": big_file.content_type,
    }
