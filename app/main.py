from fastapi import FastAPI
from app.routes import auth
from app.core.db import Base, engine
from app.models import user,application
from app.routes import application as application_routes
from app.routes import ai as ai_routes
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title = "AI Job Tracker")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded,_rate_limit_exceeded_handler)

app.include_router(auth.router)

app.include_router(application_routes.router)
app.include_router(ai_routes.router)