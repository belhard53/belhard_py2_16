from fastapi import APIRouter, Query
from schema import *
from fastapi import FastAPI, Depends
from database import UserRepository, QuizRepository, UserFilter
from fastapi_filter import FilterDepends



# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# async def home():
#    return {"data": "Hello World"}


user_router = APIRouter(
    prefix="/users",
    tags=['users1']
)

quizes_router = APIRouter(
    prefix="/quizes",
    tags=['quizes1']
)


default_router = APIRouter()



@default_router.get('/', tags=['api'])
async def index(limit='10', offset='0'):
    return {'message':'ok', 'limit':limit, 'offset':offset}

#------------------------------------

# fastapi_filter

@user_router.get('')
async def get_users(
            limit: int = Query(ge=1, default=3), 
            offset: int = Query(ge=0, default=0),
            user_filter: UserFilter = FilterDepends(UserFilter)
            ) -> dict[str, int | list[User]]:    
    users = await UserRepository.get_users(limit, offset, user_filter)
    res = {'limit':limit, 'offset':offset, 'result':users}
    return res

# a: list[int] = [1,2]
# b: dict[str, str] = {'q':'w'}

@user_router.get('/{id}')
async def get_user(id) -> User:
    user = await UserRepository.get_user(id=id)    
    return user


@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepository.add_user(user)
    return {"id":id}




@quizes_router.get('') 
async def get_quizes() -> list[Quiz]:
    quizes = await QuizRepository.get_quizes()
    return quizes