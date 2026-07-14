from fastapi import FastAPI 

app = FastAPI()

# home route
@app.get("/")
def home():
    return{"message":"welcome to home page"}