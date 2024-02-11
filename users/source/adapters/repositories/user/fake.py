from dataclasses import dataclass
from source.domain.user import User
from source.infraestructure.database.postgres import db
from source.infraestructure.database import models
from sqlalchemy import exc

@dataclass
class FakeUserRepository:

    async def save(self, user: User) -> str:
        return 1
    
    async def find_by_email(self, email: str) -> User:
        user = User()
        user.email = "fake@mail.com"
        user.password = "fake123"
        return user