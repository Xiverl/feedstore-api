from typing import List, Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_db
from src.users.sсhemas import UserCreate, UserRead, AddressCreate
from src.users.crud import create_user, get_user, get_user_list, create_address


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
    users = await get_user_list(db)
    if not users:
        raise HTTPException(status_code=404, detail="User not found")
    return users


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


@users_router.post(
    "/addresses",
    response_model=Annotated[UserRead, Depends()]
)
async def add_address(
    address: Annotated[AddressCreate, Depends()],
    db: AsyncSession = Depends(get_db)
):
    """Добавление адреса для конкретного пользователя."""
    return await create_address(address, db)
