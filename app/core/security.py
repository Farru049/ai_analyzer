# Password Hashing and JWT Token creation
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import  JWTError, jwt
from app.config import settings

pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')

def hash_password(password:str):
    if not password:
        raise ValueError("Password cannot be empty")
    return pwd_context.hash(password[:72])

def verify_password(plain_password:str, hashed_password:str):
    if not plain_password or not hashed_password:
        raise ValueError("Password and hashed password cannot be empty")
    return pwd_context.verify(plain_password[:72], hashed_password)

def create_access_token(data:dict):
    to_encode_data = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode_data.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode_data, settings.SECRET_KEY, algorithm = settings.ALGORITHM)
    return encoded_jwt
def decode_access_token(token:str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms = [settings.ALGORITHM])
        return payload
    except JWTError:
        return None