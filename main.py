from fastapi import FastAPI
from databasa import create_tables,delete_tables
from contextlib import asynccontextmanager
from views import pathsolver as tasks_router

from models import TaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI):
    #await delete_tables()
    #await create_tables()
    print ("Всё дропнуто и заново создано!")
    yield

apa = FastAPI(lifespan=lifespan)
apa.include_router(tasks_router)


