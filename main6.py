from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

class user(BaseModel):
    name:str
    age:int

@app.post("/create-user")
def create_user(user:user):
    return{
        "message":"user created",
        "data":user
    }    
print("mang loaded")