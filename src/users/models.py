from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.db import Base


class UserModel(Base):
    """Модель для хранения пользователя в БД."""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    hashed_password: Mapped[str]

    addresses = relationship("AddressModel", back_populates="user")


class AddressModel(Base):
    """Модель для хранения адрессов пользователя в БД."""
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    street: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    zip_code: Mapped[str]
    geo_x: Mapped[float]
    geo_y: Mapped[float]

    user = relationship("UserModel", back_populates="addresses")
