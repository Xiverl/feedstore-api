from fastapi import APIRouter


users_router = APIRouter(prefix="/users")


@users_router.post("")
async def add_user():
    ...


@users_router.get("")
async def get_user():
    ...


@users_router.delete("")
async def delete_user():
    ...
