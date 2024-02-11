from sqlalchemy import (
    Column,
    Integer,
    String
)
from source.infraestructure.database.postgres import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    name = Column(String(255), nullable=False)
    ipv4_address = Column(String(255), nullable=False)
