from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

todos: List[Todo] = []
next_id = 1

@app.get("/api/todos")
def get_todos():
    return todos

@app.post("/api/todos")
def create_todo(todo: dict):
    global next_id
    new_todo = Todo(id=next_id, title=todo["title"], completed=False)
    todos.append(new_todo)
    next_id += 1
    return new_todo

@app.put("/api/todos/{todo_id}")
def update_todo(todo_id: int, todo: dict):
    for t in todos:
        if t.id == todo_id:
            t.completed = todo.get("completed", t.completed)
            t.title = todo.get("title", t.title)
            return t
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/api/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos
    todos = [t for t in todos if t.id != todo_id]
    return {"message": "Todo deleted"}
