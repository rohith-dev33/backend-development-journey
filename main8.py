from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Todo CRUD API")


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str
    completed: bool

todos: List[Todo] = []



# Create Todo

@app.post("/todos", status_code=201)
def create_todo(todo: Todo):
    for item in todos:
        if item.id == todo.id:
            raise HTTPException(status_code=400, detail="Todo ID already exists")

    todos.append(todo)
    return {
        "message": "Todo created successfully",
        "data": todo
    }

# Get All Todos

@app.get("/todos")
def get_all_todos():
    return todos



# Get Todo by ID

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")



# Update Todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = Todo(
                id=todo_id,
                title=updated_todo.title,
                completed=updated_todo.completed
            )

            return {
                "message": "Todo updated successfully",
                "data": todos[index]
            }

    raise HTTPException(status_code=404, detail="Todo not found")


#delete todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)

            return {
                "message": "Todo deleted successfully",
                "data": deleted_todo
            }

    raise HTTPException(status_code=404, detail="Todo not found")