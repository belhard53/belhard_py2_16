from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select, String
from schema import UserAdd


engine = create_async_engine("sqlite+aiosqlite:///db//fastapi.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UserOrm(Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
    phone :Mapped[str|None]



# user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
        
        
async def add_test_data():
        async with new_session() as session:            
            users = [
                UserOrm(name='user1', age=11),
                UserOrm(name='user2', age=22, phone='1234567'),
                UserOrm(name='user3', age=33)
            ]    
            session.add_all(users)
                

class UserRepositoty:

    @classmethod
    async def add_user(cls, user:UserAdd) -> int:
        async with new_session() as session:
            data = user.model_dump()
            user = UserOrm(**data)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id
        
    @classmethod
    async def get_users(cls) -> list[UserOrm]:
        async with new_session() as session:
            query = select(UserOrm)
            res = await session.execute(query)
            users = res.scalars().all()
            return users
        
    @classmethod
    async def get_user(cls, id:int) -> UserOrm:
        async with new_session() as session:
            query = select(UserOrm).filter(UserOrm.id==id)
            # query = text("select int_id from table")            
            res = await session.execute(query)
            user = res.scalars().first() #scalar - преобр в список
            return user