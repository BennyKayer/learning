"""https://fastapi.tiangolo.com/tutorial/request-files/
What Upload File has
https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile
"""
from typing import List
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    """Example of File parameter usage
    with bytes
    THIS WILL CAUSE FILE TO BE IN MEMORY"""
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """Advantages of UploadFile over bytes
    - file is stored in memory up to a limit then on a disk
    - can access metadata
    - async interface
    - Exposes SpooledTemporaryFile that other libraries usually expect
    """
    content = await file.read()
    return {"filename": file.filename, "content": content}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    """This is how to create endpoint that accepts multiple files"""
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    """[summary]"""
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
