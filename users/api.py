from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from db import get_db
from users.sсhemas import UserCreate, UserRead, AddressCreate, Address
from users.crud import create_user, get_user


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("", response_model=UserRead)
async def add_user(
    user: UserCreate = None, db: AsyncSession = Depends(get_db)
):
    """Добавление нового пользователя."""
    return await create_user(user, db)


@users_router.get("", response_model=List[UserRead])
async def read_users(
    skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)
):
    """Получение списка пользователей с пагинацией."""
    return {"msg": "Отображаем информацию о существующих пользователях"}


@users_router.get("/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Получение конкретного пользователя по ID."""
    user = await get_user(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@users_router.delete("/{user_id}")
async def remove_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Удаление пользователя по ID."""
    return {"msg": f"Удаляем пользователя №{user_id}"}


@users_router.post("/{user_id}/addresses", response_model=Address)
async def add_address(
    user_id: int, address: AddressCreate, db: AsyncSession = Depends(get_db)
):
    """Добавление адреса для конкретного пользователя."""
    return {"msg": f"Добавляем новый адресс для пользователя №{user_id}"}
