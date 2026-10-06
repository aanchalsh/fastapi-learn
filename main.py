from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def get_read():
    return { 
        "message": "Hello test get api"
    }

@app.post("/greet")
def greet_message(name: str):
    return {
        "message": f"Hello, {name}!"    }
