from pydantic import BaseModel, Field
from pydantic.networks import IPvAnyAddress

class Team(BaseModel):
    id: int | None = None
    user_id: int = Field()
    name: str = Field(min_length=6, max_length=12)
    ipv4_address: IPvAnyAddress
