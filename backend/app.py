
from fastapi import FastAPI
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShieldPME API",
    description="Cybersecurity monitoring platform for SMEs",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ShieldPME!",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ShieldPME Backend",
        "database": "connected"
    }

@app.get("/database/tables")
def database_tables():
    return {
        "tables": list(Base.metadata.tables.keys())
    }
