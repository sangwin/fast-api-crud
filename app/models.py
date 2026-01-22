from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: str
    age: int

class UserCreate(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
