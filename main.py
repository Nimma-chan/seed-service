import os

import psycopg

from fastapi import FastAPI

app = FastAPI()

# Приветствие сервис берёт из окружения.
# Нет переменной GREETING — сервис не стартует.
greeting = os.environ["GREETING"]

@app.get("/")
def read_root():
    return {"message": greeting}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/db-check")
def db_check():
    database_url = os.environ["DATABASE_URL"]
    with psycopg.connect(database_url) as conn:
        conn.execute("SELECT 1")
    return {"db": "ok"}