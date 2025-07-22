from typing import List

from pydantic import BaseModel, EmailStr


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str


class AddressCreate(AddressBase):
    pass


class Address(AddressBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    addresses: List[Address] | None = None

    class Config:
        from_attributes = True
