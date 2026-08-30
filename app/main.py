import os
from fastapi import FastAPI

app = FastAPI(title="FastAPI + Docker + Poetry")

@app.get("/")
def read_root():
    env = os.getenv("APP_ENV", "not set")
    return {"status": "ok", "environment": env}
