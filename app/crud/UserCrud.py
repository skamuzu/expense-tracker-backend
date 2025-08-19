from schemas.UserSchema import UserCreate
from sqlalchemy.orm import Session
from models.UserModel import User
from auth.security import hash_password


def create_user(user: UserCreate, db:Session):
    db_user = User(name=user.name, email = user.email, hashed_password=hash_password(password=user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



