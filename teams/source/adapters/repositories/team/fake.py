from dataclasses import dataclass
from source.domain.team import Team

@dataclass
class FakeUserRepository:

    async def save(self, team: Team) -> str:
        return 1
    
    async def find(self, email: str) -> Team:
        team = Team()
        team.id = 1
        team.user_id = 1
        team.name = "fake"
        team.ipv4_address = "8.8.8.8"
        return team