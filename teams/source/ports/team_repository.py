from abc import ABC, abstractmethod
from typing import List
from source.domain.team import Team


class TeamRepository(ABC):
    @abstractmethod
    async def save(self, team: Team) -> int:
        raise NotImplementedError
    @abstractmethod
    async def list(self) -> List[Team]:
        raise NotImplementedError
    @abstractmethod
    async def get(self, id: int) -> Team:
        raise NotImplementedError
    @abstractmethod
    async def find(self, id: int) -> Team:
        raise NotImplementedError
    @abstractmethod
    async def update(self, team: Team):
        raise NotImplementedError
    @abstractmethod
    async def delete(self, id: int):
        raise NotImplementedError
