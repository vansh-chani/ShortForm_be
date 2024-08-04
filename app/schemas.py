from pydantic import BaseModel
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str  # Changed to password instead of hashed_password

class User(UserBase):
    id: int
    hashed_password: str  # Include hashed_password in the response schema

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class CreatorBase(BaseModel):
    name: str
    job_description: str
    genre: str
    sub_genre: str

class CreatorCreate(CreatorBase):
    pass

class Creator(CreatorBase):
    id: int
    user_id: int
    pricings: List['Pricing'] = []

    class Config:
        orm_mode = True

class PricingBase(BaseModel):
    description: str
    delivery_time: int
    time_limit: float
    content_form: str
    price: float
    type: str

class PricingCreate(PricingBase):
    pass

class Pricing(PricingBase):
    id: int
    creator_id: int

    class Config:
        orm_mode = True
