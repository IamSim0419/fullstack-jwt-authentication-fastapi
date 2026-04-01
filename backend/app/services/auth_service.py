from app.repositories.user_repository import UserRepository
from app.core.security import (hash_password, verify_password, create_access_token)

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, email: str, password: str):
        if self.repo.get_by_email(email):
            raise ValueError("Email already registered!")
        return self.repo.create(email, hash_password(password))
    
    def login(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid credentials!")
        return create_access_token(user.email)
    



    