# pip install fastapi 
#       uvicorn pydantic aiosqlite sqlalchemy

from fastapi import FastAPI
from schema import UserAdd, User, UserId
from contextlib import asynccontextmanager
from database import create_tables, delete_tables, add_test_data
from router import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await add_test_data()
    print("------Bases build-------------")
    yield
    await delete_tables()
    print("-------------Bases droped------------")


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
# app.include_router(quiz_router)
