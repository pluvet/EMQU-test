from dataclasses import dataclass

from source.ports.team_repository import TeamRepository
from source.domain.team import Team
from typing import List

@dataclass
class TeamCrudService():
    team_repo: TeamRepository

    async def create(self, user_id: int,name: str, ipv4_address: str) -> int:
        
        new_team = Team(id=None, user_id=user_id ,name=name, ipv4_address=ipv4_address)
        return await self.team_repo.save(team=new_team)
    
    async def update(self, id: int, name: str, ipv4_address: str):
        
        team = await self.team_repo.find(id)
        team.name = name
        team.ipv4_address = ipv4_address
        await self.team_repo.update(team=team)
    
    async def list(self) -> List[Team]:
        
        return  await self.team_repo.list()
    
    async def get(self, id: int) -> Team:
        return  await self.team_repo.find(id)
    
    async def delete(self, id: int):
        return await self.team_repo.delete(id)
