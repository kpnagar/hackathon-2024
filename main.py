import os

import requests
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks, status, UploadFile, File
from fastapi.responses import JSONResponse
import json
from service import ask_ai

app = FastAPI()


@app.get("/")
async def index():
    return JSONResponse(content={"received": True}, status_code=status.HTTP_200_OK)


@app.post("/ask")
async def ask(request: Request, text: str):
    try:
        data = {"text": text}
        res = await ask_ai(text)
        answer = res['answer']
        print(answer)
    except Exception as e:
        return JSONResponse(content={"Error": str(e)}, status_code=status.HTTP_400_BAD_REQUEST)
    return JSONResponse(content={"data": answer}, status_code=status.HTTP_200_OK)
