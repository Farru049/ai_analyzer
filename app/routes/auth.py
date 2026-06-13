# receive HTTP request, call service, return HTTP response. Nothing else.
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.auth_service import register_user, login_user
from app.schemas.user import UserCreate, UserResponse, TokenResponse

router = APIRouter(prefix = "/auth", tags = ["auth"])

@router.post("/register", response_model = UserResponse)
def register(user_data:UserCreate, db:Session = Depends(get_db)):
    return register_user(db, user_data)

@router.post("/login", response_model = TokenResponse)
def login(user_data:UserCreate, db:Session = Depends(get_db)):
    
    return login_user(db, user_data.email, user_data.password)