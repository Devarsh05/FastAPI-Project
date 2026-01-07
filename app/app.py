from fastapi import FastAPI

app = FastAPI()

@app.get("/hello-wold")
def hello_world():
    return {"message": "Hello World"}

