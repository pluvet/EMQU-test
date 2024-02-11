from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int | None = None
    email: EmailStr
    password: str = Field(min_length=6, max_length=12)
