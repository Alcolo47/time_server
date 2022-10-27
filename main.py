from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"time": datetime.now().timestamp()}
