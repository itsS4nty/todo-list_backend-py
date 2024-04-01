from fastapi import FastAPI
from controller import addDuty, delDuty, getDuties, updDuty
from database.connect import cursor
from lib.schemas.mainSchemas import validateSchema
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from models import CreateDuty, DeleteDuty, UpdateDuty

@asynccontextmanager
async def lifespan(_: FastAPI):
    print('Init')
    cursor.execute('''CREATE TABLE IF NOT EXISTS duties(
            id SERIAL,
            name VARCHAR(255) NOT NULL,
            status INTEGER NOT NULL,
            created_at BIGINT NOT NULL,
            modified_at BIGINT NOT NULL
        );''')
    yield
    # cursor.close()
    print('end')

app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"greeting":"Hello world"}

@app.get('/duty')
async def getDuty(status: int):
    data = validateSchema('FindDuties', status)
    return_data = getDuties(data)
    return return_data

@app.post('/duty')
async def createDuty(duty: CreateDuty):
    res = addDuty(duty.name)
    return res

@app.put('/duty')
async def updateDuty(duty: UpdateDuty):
    return updDuty(duty.id, duty.status)

@app.delete('/duty')
async def deleteDuty(duty: DeleteDuty):
    print(duty)
    return delDuty(duty.id, duty.fullDelete)
