import time

# fastapi
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import StreamingResponse
from pydantic import BaseModel

# logging
import logging
logger = logging.getLogger("api")

# Environment variables

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'])

@app.get('/time')
def time():
    return time.time()
