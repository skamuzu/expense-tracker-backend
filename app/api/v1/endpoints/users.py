from fastapi import APIRouter
from crud.UserCrud import create_user
from core.dependencies import db_dependency
from schemas.UserSchema import UserCreate, UserRead
from auth.security import get_current_user


user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.post("/",response_model=UserRead)
async def register_user(user:UserCreate, db:db_dependency):
    return create_user(user,db)


    