from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables


@asynccontextmanager
async def lifespan():
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int


tasks = []

# @app.get("/tasks")
# def get_tasks():
#     task = STask(name="Some task")
#     return {"data": task}

@app.post("/tasks")
async  def add_task(task: STaskAdd):
    tasks.append(task)
    return {"ok": True}
