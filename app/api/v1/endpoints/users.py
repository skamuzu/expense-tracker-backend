from fastapi import APIRouter
from crud.UserCrud import create_user
from core.dependencies import db_dependency
from main import app
from schemas.UserSchema import UserCreate


router = APIRouter(prefix="/users", tags=["users"])

@router.post("/",response_model=UserCreate)
async def register_user(user:UserCreate, db=db_dependency):
    return create_user(user,db)
