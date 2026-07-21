from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
 age:int
 name:str
 password:str

class UserResponse(BaseModel):
  name:str
  age:int

@app.get("/user", response_model=UserResponse)
def get_user():
    return{
     "name":"rohith",
        "age":33,
        "password":"33343"
      }


      
 