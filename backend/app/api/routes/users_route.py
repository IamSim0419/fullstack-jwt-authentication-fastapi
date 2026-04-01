from fastapi import APIRouter, Depends
from app.core.dependencies import get_current_user

router = APIRouter(prefix="users", tags=["users"])


@router.get("/me")
def me(current_user: str = Depends(get_current_user)):
    return {"username": current_user}




