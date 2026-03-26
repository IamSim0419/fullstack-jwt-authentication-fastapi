from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str):
    return pwd_context.verify(password, hashed)

def create_access_token(data: dict, expires_delta: int):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(datetime.UTC) + timedelta
    else:
        expire = datetime.now(datetime.UTC) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
