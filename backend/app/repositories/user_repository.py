from sqlalchemy.orm import Session
from app.db.models import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
    
    def create(self, email: str, password: str):
        new_user = User(email=email, password=password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user