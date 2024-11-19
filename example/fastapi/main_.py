# pip install fastapi,  uvicorn, pydantic, aiosqlite, sqlalchemy

# gunicorn - синхронно

from pydantic import BaseModel
from fastapi import FastAPI, Depends
import uvicorn

app = FastAPI()

class STaskAdd(BaseModel):
   name: str
   description: str | None = None



@app.get('/', tags='Hello')
async def home():
    return {"name":"name1"}


@app.post("/")
async def add_task(task: STaskAdd = Depends()):
    return {"data": task}



if __name__ == '__main__':    
    uvicorn.run ("main:app", reload=True) 
    
    
# консоль
# uvicorn main:app --reload    
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload 