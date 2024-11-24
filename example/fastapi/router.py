from fastapi import APIRouter
from schema import *
from fastapi import FastAPI, Depends
from database import UserRepository, QuizRepository



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
async def index():
    return {'message':'ok'}



@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepository.add_user(user)
    return {"id":id}


@user_router.get('')
async def get_users() -> list[User]:
    users = await UserRepository.get_users()
    return users


@user_router.get('/{id}')
async def get_user(id) -> User:
    user = await UserRepository.get_user(id=id)    
    return user


@quizes_router.get('') 
async def get_quizes() -> list[Quiz]:
    quizes = await QuizRepository.get_quizes()
    return quizes