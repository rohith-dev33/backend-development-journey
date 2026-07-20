from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

users = []

class user(BaseModel):
    name:str
    age:int
@app.post("/users")
def create_user(user:user):
    users.append(user)
    return{
       "message":"user created",
       "data":user

   }

@app.put("/users/{user_id}")
def updated_user(user_id:int,user:user ,notify:bool = False):
    if user_id < len(users):
        users[user_id]=user

        return{
            "message":"user updated",
            "notify":notify,
            "data":user
        }
    return{
        "error":"user not found"
    }