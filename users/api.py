from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db import get_db
from users.shemas import UserCreate, User, AddressCreate, Address


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("", response_model=User)
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """Добавление нового пользователя."""
    ...


@users_router.get("", response_model=List[User])
async def read_users(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Получение списка пользователей с пагинацией."""
    ...


@users_router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Получение конкретного пользователя по ID."""
    ...


@users_router.delete("/{user_id}")
async def remove_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Удаление пользователя по ID."""
    ...


@users_router.post("/{user_id}/addresses", response_model=Address)
async def add_address(
    user_id: int, address: AddressCreate, db: AsyncSession = Depends(get_db)
):
    """Добавление адреса для конкретного пользователя."""
    ...
