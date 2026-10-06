from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def get_read():
    return { 
        "message": "Hello test get api"
    }