
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]= None
    valid: bool

tasks = []
valid = [True, False]
for i in range(1, 11):
    new_task = Task(
        id=i,
        title=f"title{i}",
        description=f"description{i}",
        valid=True
    )
    tasks.append(new_task)

@app.get("/tasks/")
async def get_tasks():

    actual_tasks=[]
    for task in tasks:
        if task.valid==True:
            actual_tasks.append(task)

    return actual_tasks if actual_tasks else {"message":"No actual tasks found"}

@app.get("/task/")
async def get_task_by_id(task_id: int):
    for t in tasks:
        if t.id == task_id and t.valid==True:
            return t
    return  {"message":"No such ID found"}

@app.post("/task/")
async def create_task(task:Task):
    tasks.append(task)
    return task

@app.put("/tasks/")
async def update_task(task_id: int,task:Task):
    for i,t in enumerate(tasks):
        if t.id == task_id:
            tasks[i]=task

            return tasks
    return {"message": "task not found"}

@app.delete("/task/")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.valid=False
            return {"message": "task removed"}
    return {"message": "task not found"}
