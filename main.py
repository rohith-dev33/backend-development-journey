from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"heelon world vern"}