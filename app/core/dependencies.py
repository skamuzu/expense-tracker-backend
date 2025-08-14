from fastapi import Depends
from typing import Annotated, Generator
from databases import SessionLocal
from sqlalchemy.orm import Session


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency: Annotated[Session, Depends(get_db)]
