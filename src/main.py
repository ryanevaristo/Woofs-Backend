from pip import List
import uvicorn

from fastapi import FastAPI

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from fastapi_sqlalchemy import DBSessionMiddleware, db

import os
from dotenv import load_dotenv
from routes import AnimalRoutes


load_dotenv('.env')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(AnimalRoutes.router)
#app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
def read_root():
    return {"User": "Teste"}

@app.get("/item/{id}}")
def read_user(id:int, q: bool | None = None):
    return {"id": id, "q": q}

@app.get("/user/")
def read_user(id:int = 0):
    if(id == 0):
        return {"users": []}
    return {"id": id}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)