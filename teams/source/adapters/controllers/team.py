from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from source.infraestructure.framework.middleware import BearerTokenAuthBackend
from source.domain.team import Team
from source.services.team import TeamCrudService

from source.adapters.repositories.team.postgres import TeamRepository
team_router = APIRouter()

@team_router.post('/')
async def create(request: Request, user_id = Depends(BearerTokenAuthBackend()))-> JSONResponse:
    """this function creates a new team"""
    request = await request.json()

    team_repository = TeamRepository()
    team_crud_service = TeamCrudService(team_repository)

    team_id = await team_crud_service.create(
        user_id=user_id,
        name=request["name"],
        ipv4_address=request["ipv4_address"],
    )

    return JSONResponse({"team_id": team_id}, status_code=201)

@team_router.get('/')
async def list()-> JSONResponse:
    """this function list all team"""

    team_repository = TeamRepository()
    team_crud_service = TeamCrudService(team_repository)

    teams = await team_crud_service.list()
    
    teams_json = jsonable_encoder(teams)

    return JSONResponse(teams_json, status_code=200)

@team_router.get('/{id}')
async def get(id: int)-> JSONResponse:
    """this function get one team"""

    team_repository = TeamRepository()
    team_crud_service = TeamCrudService(team_repository)

    team = await team_crud_service.get(id)
    
    team_json = jsonable_encoder(team)

    return JSONResponse(team_json, status_code=200)

@team_router.put('/{id}', dependencies=[Depends(BearerTokenAuthBackend())])
async def put(id: int, request: Request)-> JSONResponse:
    """this function update one team"""
    request = await request.json()

    team_repository = TeamRepository()
    team_crud_service = TeamCrudService(team_repository)

    await team_crud_service.update(
        id=id,
        name=request["name"],
        ipv4_address=request["ipv4_address"],
    )

    return JSONResponse({}, status_code=200)

@team_router.delete('/{id}')
async def delete(id: int)-> JSONResponse:
    """this function delete one team"""

    team_repository = TeamRepository()
    team_crud_service = TeamCrudService(team_repository)

    await team_crud_service.delete(id)

    return JSONResponse(None, status_code=204)
