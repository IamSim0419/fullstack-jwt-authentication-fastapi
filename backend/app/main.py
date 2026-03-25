from fastapi import FastAPI, HTTPException, status
from sqlalchemy.orm import Session


from passlib.context import CryptContext
from models import User
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()



origins = [
    "http://localhost:3000",
    "http://yourfrontenddomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Allows all origins from the list
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods
    allow_headers=["*"], # Allows all headers
)










