from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from core.databases import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length=100))  # you can adjust length
    email: Mapped[str] = mapped_column(String(length=255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(length=255))
    image_url: Mapped[str | None] = mapped_column(String(length=255), nullable=True)
