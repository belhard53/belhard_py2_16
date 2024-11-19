from fastapi import APIRouter
from schema import *
from fastapi import FastAPI, Depends
from database import UserRepositoty



user_router = APIRouter(
    prefix="/users",
    tags=['users']
)



@user_router.post('')
async def add_user(user: UserAdd = Depends()) -> UserId:
    id = await UserRepositoty.add_user(user)
    return {"id":id}


@user_router.get('')
async def get_users() -> list[User]:
    users = await UserRepositoty.get_users()
    return users


# Дописать
#@user_router.get('/{id}')