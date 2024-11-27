from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import select, Integer, ForeignKey, String, Table, Column
from schema import UserAdd
from fastapi_filter.contrib.sqlalchemy import Filter


engine = create_async_engine("sqlite+aiosqlite:///db//fastapi.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UserOrm(Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    age: Mapped[int]
    phone :Mapped[str|None]
    quiz = relationship('QuizOrm', backref='user')


class UserFilter(Filter):
    name: str | None = None
    name__like: str | None = None
    name__startswith: str | None = None
    phone__in: list[str] | None = None
    # для in перечисление через запятую без пробела
    # http://127.0.0.1:8100/users?limit=3&offset=0&phone__in=11,22 
    
    
    
    order_by: list[str] = ['age']
    # для обратной сортировки перед именем поля добавить минус
    # http://127.0.0.1:8100/users?limit=5&offset=0&order_by=-age
    # если сортировка по нескольким полям - поля указывать чз запятую без пробела
    # http://127.0.0.1:8100/users?limit=5&offset=0&order_by=age,name
    class Constants(Filter.Constants):
        model = UserOrm



'''
добавляются к названию поля через два "_"

Сравнительные операторы :
    eq: равно
    neq(или ): не равно not
    gt: больше
    lt: меньше
    gte: больше или равно
    lte: меньше или равно
Операторы для работы с коллекциями :
    in: принадлежит множеству
    not_in: не принадлежит множеству
Операторы для строковых данных :
    like: соответствует шаблону 
    ilike: регистронезависимый поиск по шаблону
    startswith: начинается с
    endswith:кончается на
    contains:содержит подстроку
    not_like: не соответствует шаблону
Специальные операторы :
    isnull: проверка на NULL
    not_isnull:проверка на NOT NULL

'''




quiz_question = Table('quiz_question', Model.metadata,
                      Column('quiz_id', ForeignKey('quiz.id'), primary_key=True),
                      Column('question_id', ForeignKey('question.id'), primary_key=True)
                      )


class QuizOrm(Model):
    __tablename__ = 'quiz'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    question = relationship("QuestionOrm", secondary="quiz_question", back_populates='quiz')


class QuestionOrm(Model):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(500))
    answer: Mapped[str] = mapped_column(String(100))
    wrong1: Mapped[str] = mapped_column(String(100))
    wrong2: Mapped[str] = mapped_column(String(100))
    wrong3: Mapped[str] = mapped_column(String(100))
    quiz = relationship("QuizOrm", secondary="quiz_question", back_populates='question')


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def add_test_data():
    async with new_session() as session:
        users = [
            UserOrm(name='user1', age=20),
            UserOrm(name='user2', age=30, phone='123456789'),
            UserOrm(name='user3', age=41, phone='11'),
            UserOrm(name='user4', age=42, phone='22'),
            UserOrm(name='user5', age=43, phone='33'),
            UserOrm(name='user6', age=44),
            UserOrm(name='user7', age=45),
            UserOrm(name='user8', age=46),
            UserOrm(name='user9', age=47),
            UserOrm(name='user10', age=40),
            UserOrm(name='user11', age=40),
            UserOrm(name='user12', age=40),
            UserOrm(name='user13', age=40),
            UserOrm(name='user14', age=40),
            UserOrm(name='user13', age=40),
        ]
        quizzes = [
            QuizOrm(name='quiz1', user=users[0]),
            QuizOrm(name='quiz2', user=users[1]),
            QuizOrm(name='quiz3', user=users[2])
        ]
        questions = [
            QuestionOrm(question='Сколько будeт 2+2*2', answer='6',
                        wrong1='8', wrong2='2', wrong3='0'),
            QuestionOrm(question='Сколько месяцев в году имеют 28 дней?', answer='Все',
                        wrong1='Один', wrong2='Ни одного', wrong3='Два'),
            QuestionOrm(question='Какой рукой лучше размешивать чай?', answer='Ложкой',
                        wrong1='Правой', wrong2='Левой', wrong3='Любой')
        ]
        quizzes[0].question.append(questions[0])
        quizzes[0].question.append(questions[1])
        quizzes[1].question.append(questions[1])
        quizzes[1].question.append(questions[2])
        quizzes[2].question.append(questions[0])
        quizzes[2].question.append(questions[2])

        session.add_all(quizzes)
        session.add_all(users[3:])
        
        
        await session.flush()
        await session.commit()

class UserRepository:
        
    @classmethod
    async def add_user(cls, user:UserAdd) -> int:
        async with new_session() as session:
            data = user.model_dump()
            # print(data)
            user = UserOrm(**data)            
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id
        
    @classmethod
    async def get_users(cls, limit, offset, user_filter) -> list[UserOrm]:
        async with new_session() as session:
            
            query = select(UserOrm) #.join()
            query = user_filter.filter(query).limit(limit).offset(offset) 
            query = user_filter.sort(query)
            # для обратной сортировки перед именем поля добавить минус
            # http://127.0.0.1:8100/users?limit=5&offset=0&order_by=-age
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
        
class QuizRepository:
    
    @classmethod
    async def get_quizes(cls) -> list[QuizOrm]:
        async with new_session() as session:
            query = select(QuizOrm)
            res = await session.execute(query)
            quizes = res.scalars().all()
            return quizes