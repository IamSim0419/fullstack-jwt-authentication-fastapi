from sqlalchemy.orm import Session
from models import User
from schemas.user_schema import UserCreate
from passlib.context import CryptContext
from fastapi.routing import APIRouter, HTTPException, status, Depends
from db_session import get_db
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt", ], deprecated="auto")

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/register" )
def register(user: UserCreate, db: Session = Depends(get_db())):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db, user)

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db())):
    user = get_user_by_username(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    # Here you would create and return a JWT token
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}

