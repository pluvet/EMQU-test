from fastapi import FastAPI
from source.adapters.controllers.team import team_router
from source.infraestructure.database import postgres, models

app = FastAPI()
models.Base.metadata.create_all(bind=postgres.engine)

app.include_router(team_router, prefix='/teams')

