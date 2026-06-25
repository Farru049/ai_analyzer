from fastapi import FastAPI
from app.routes import auth
from app.core.db import Base, engine
from app.models import user,application
from app.routes import application as application_routes
from app.routes import ai as ai_routes

app = FastAPI(title = "AI Job Tracker")

app.include_router(auth.router)
app.include_router(application_routes.router)
app.include_router(ai_routes.router)