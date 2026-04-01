from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.schemas.auth_schema import RegisterSchema, LoginSchema, TokenSchema

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    service = AuthService(user_repo)
    try:
        service.register(data.email, data.password)
        return {"message": "User registered successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login", response_model=TokenSchema)
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user_repo = UserRepository(db)
    service = AuthService(user_repo)
    try:
        token = service.login(data.email, data.password)
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    



