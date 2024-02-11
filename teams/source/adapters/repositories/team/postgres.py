from dataclasses import dataclass
from source.domain.team import Team
from source.infraestructure.database.postgres import db
from source.infraestructure.database import models
from typing import List
from sqlalchemy import exc

@dataclass
class TeamRepository:

    async def save(self, team: Team) -> str:
        team.ipv4_address = str(team.ipv4_address)
        team = models.Team(**team.model_dump())
        try:
            db.add(team)
            db.commit()
            db.refresh(team)
        except exc.IntegrityError:
            db.flush()
            db.rollback()
        return team.id
    
    async def find(self, id: int) -> models.Team:
        team = db.query(models.Team).filter(models.Team.id == id).first()
        return team
    
    async def list(self) -> List[dict]:
        teams = db.query(models.Team).all()
        return teams
    
    async def update(self, team: models.Team) -> List[Team]:
        db.commit()
        db.refresh(team)
        
    async def delete(self, id: int):
        team = await self.find(id)
        db.delete(team)
        db.commit()
