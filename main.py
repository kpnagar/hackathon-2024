import os

import requests
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks, status, UploadFile, File
from fastapi.responses import JSONResponse
import json

app = FastAPI()


@app.get("/")
async def index():
    return JSONResponse(content={"received": True}, status_code=status.HTTP_200_OK)

