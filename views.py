from databasa import TaskTable
from models import TaskAdd, TaskRead, TaskId
from fastapi import APIRouter

from repo import TaskRepos

pathsolver=APIRouter(prefix='/fastapp')

@pathsolver.get("/tasks")
async def get_tasks() -> list[TaskRead]:
    tasks=await TaskRepos.find()
    return tasks

@pathsolver.post("/add")
async def add_task(task:TaskAdd)->TaskId:
    tId=await TaskRepos.add(task)
    return {"id":tId,"status":True}