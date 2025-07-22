from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.users.sсhemas import UserCreate, UserRead
from src.users.models import UserModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user: UserCreate, session: AsyncSession) -> UserRead:
    """Создания пользователя в БД.

    Args:
        user (UserCreate): Обьект схемы для создание пользователя.
        session (AsyncSession): Ассинхронная ссесия для запросов в БД.

    Returns:
        UserRead: Обьект схемы для чтения пользователя.
    """
    hashed_password = pwd_context.hash(user.password)

    db_user = UserModel(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hashed_password
    )

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)

    return UserRead(
        id=db_user.id,
        email=db_user.email,
        first_name=db_user.first_name,
        last_name=db_user.last_name,
        addresses=[]
    )


async def get_user(user_id: int, session: AsyncSession) -> UserModel | None:
    stmt = (
        select(UserModel)
        .where(UserModel.id == user_id)
        .options(selectinload(UserModel.addresses))
    )
    result = await session.execute(stmt)
    return result.scalars().first()


async def get_user_list(session: AsyncSession) -> List[UserModel]:
    """Чтение информаци о конкретном пользователе из БД.

    Args:
        user_id (int): ID пользователя.
        session (AsyncSession): Ассинхронная ссесия для запросов в БД.

    Returns:
        UserRead | None: Обьект схемы для чтения пользователя.
    """
    stmt = (
        select(UserModel)
        .options(selectinload(UserModel.addresses))
    )
    result = await session.execute(stmt)
    return result.scalars().all()
