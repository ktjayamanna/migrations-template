from fastapi import FastAPI

app = FastAPI(title="Write Microservice", version="1.0.0")

@app.get("/ping")
async def ping():
    return {"message": "Write service is up and running!"}
