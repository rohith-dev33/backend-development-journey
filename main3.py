from fastapi import FastAPI 

app = FastAPI()

# home route
@app.get("/")
def home():
    return{"message":"welcome to home page"} 

#about route 
@app.get("/about")
def about():
    return{"message":"this is about secrion"}

#users route 
@app.get("/users")
def users():
    return{"message":"this is user page"}