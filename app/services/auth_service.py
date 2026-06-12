from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.core.security import verify_password, create_access_token, hash_password
from app.models.user import UserCreate

def register_user(db:Session, user_data:UserCreate):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Email already registered")
    hashed = hash_password(user_data.password)
    new_user = User(email = user_data.email, hashed_password = hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def login_user(db:Session, email:str, password:str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid email or password")
    access_token = create_access_token(data = {"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}