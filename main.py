from fastapi import FastAPI
import uvicorn
from schemas import TaskCreate, TaskResponse

app = FastAPI()

@app.get("/")

def root():
    return {"message": "Hello? world!!"}

@app.post("/tasks/", response_model=TaskResponse)
async def create_task(task: TaskCreate):
    new_task = task.dict()
    new_task["id"] = 1
    new_task["is_done"] = False
    return new_task

