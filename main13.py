from fastapi import FastAPI,Depends,Header,HTTPException

app =FastAPI()

def verify_token(token:str = Header(None)):
    if token != "my secrettoken":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"
        )
    return{
        "user":"authorized user"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return{
        "message":"secure data acssesed",
        "user":user
    }
        