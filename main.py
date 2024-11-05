from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import os
import uuid

app = FastAPI()

db = []


@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    db.append(contents)

    return {"filename": file.filename}