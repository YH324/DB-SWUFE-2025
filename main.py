from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI()

class SQLRequest(BaseModel):
    sql: str

def get_connection():
    return psycopg2.connect(
        dbname=os.environ.get("DB_NAME", "postgres"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres"),
        host=os.environ.get("DB_HOST", "localhost"),
        port=os.environ.get("DB_PORT", "5432")
    )

@app.post("/validate")
def validate_sql(req: SQLRequest):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"EXPLAIN {req.sql}")
        cur.close()
        conn.close()
        return {"valid": True, "message": "✅ SQL 语法有效"}
    except Exception as e:
        return {"valid": False, "error": str(e)}
