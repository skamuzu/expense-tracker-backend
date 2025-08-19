from fastapi import APIRouter
from crud.UserCrud import create_user
from core.dependencies import db_dependency
from schemas.UserSchema import UserCreate, UserRead
from crud.UserCrud import login_for_access_token


user_router = APIRouter(prefix="/users", tags=["users"])
token_router = APIRouter(prefix="/token", tags=["auth"])

@user_router.post("/",response_model=UserRead)
async def register_user(user:UserCreate, db:db_dependency):
    return create_user(user,db)

@token_router.post("/access")
async def login_user(user:UserCreate):
    return login_for_access_token(user)
    