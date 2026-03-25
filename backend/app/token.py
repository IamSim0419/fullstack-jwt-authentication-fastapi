
from datetime import datetime, timedelta

from jose import jwt, JWTError
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


#Create access token
def create_access_token(data: dict, expires_delta: int = 30):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(datetime.UTC) + timedelta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




