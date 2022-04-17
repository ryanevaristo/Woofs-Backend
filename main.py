from pip import List
import uvicorn

from fastapi import FastAPI

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
#from fastapi_sqlalchemy import DBSessionMiddleware, db

import os
from dotenv import load_dotenv
from routes import  UsuarioRoutes


load_dotenv('.env')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(UsuarioRoutes.router)
#app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)