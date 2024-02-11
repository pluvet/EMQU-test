from dataclasses import dataclass

from source.ports.user_repository import UserRepository
import jwt

secret = "D3AAB54D5ADE7F17D4407BD50FD02648AE563BAA64939E49ED938E675240A709"
@dataclass
class LoginUserService():
    user_repo: UserRepository

    async def execute(self, email: str, password: str) -> bool:
        
        user = await self.user_repo.find_by_email(email)
        if user.password != password:
            return False
        encoded_jwt = jwt.encode({"user_id": user.id}, secret, algorithm="HS256")
        return encoded_jwt