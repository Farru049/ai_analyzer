from fastapi import FastAPI
from app.routes import auth
from app.core.db import Base, engine

Base.metadata.create_all(bind = engine)

app = FastAPI(title = "AI Job Tracker")

app.include_router(auth.router)