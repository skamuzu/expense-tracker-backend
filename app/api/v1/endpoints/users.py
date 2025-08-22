from fastapi import APIRouter, Depends, HTTPException, status
from crud.UserCrud import create_user
from core.dependencies import db_dependency
from schemas.UserSchema import UserCreate, UserRead
from auth.security import get_current_user, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated
from schemas.TokenSchema import Token
from datetime import timedelta
from auth.forms import EmailPasswordRequestForm




user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/",response_model=UserRead)
async def register_user(user:UserCreate, db:db_dependency):
    return create_user(user,db)

@user_router.post("/login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[EmailPasswordRequestForm, Depends()],
    db: db_dependency
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")