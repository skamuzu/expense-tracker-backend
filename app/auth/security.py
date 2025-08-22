from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from core.dependencies import db_dependency
from schemas.UserSchema import UserInDB
from schemas.TokenSchema import TokenData, Token
from sqlalchemy import select
from models.UserModel import User
from core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5

def hash_password(password:str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)



def get_user(user: str, db: db_dependency):
    stmt = select(User).where(User.email == user)
    result = db.execute(stmt).scalar_one_or_none()
    return result 


def authenticate_user(db: db_dependency, email: str, password: str):
    user = get_user(email, db)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: db_dependency):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(token_data.email, db)
    if user is None:
        raise credentials_exception
    return user

    

