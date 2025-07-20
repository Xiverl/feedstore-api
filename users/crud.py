from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.future import select
from users.sсhemas import UserCreate, UserRead
from users.models import UserModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(user: UserCreate, session: AsyncSession) -> UserRead:
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


async def get_user(user_id: int, session: AsyncSession) -> UserRead | None:
    db_user = await session.get(UserModel, user_id)
    if not db_user:
        return
    return UserRead(
        id=db_user.id,
        email=db_user.email,
        first_name=db_user.first_name,
        last_name=db_user.last_name,
        addresses=[]
    )
