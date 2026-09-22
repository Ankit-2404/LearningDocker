from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My FastAPI app is running in Docker!"}

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Learn Docker"},
        {"id": 2, "title": "Learn FastAPI"}
    ]