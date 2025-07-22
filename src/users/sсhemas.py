from typing import List

from pydantic import BaseModel, EmailStr, ConfigDict


class AddressBase(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    geo_x: float
    geo_y: float


class AddressCreate(AddressBase):
    user_id: int


class Address(AddressBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    addresses: List[Address] | None = None

    model_config = ConfigDict(from_attributes=True)
