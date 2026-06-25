from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# ← add your app to path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# ← import your Base and models
from app.core.db import Base
from app.models import user, application   # ← import ALL models

config = context.config

# ← set DB URL from environment variable
from app.config import settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

fileConfig(config.config_file_name)

# ← tell alembic about your models
target_metadata = Base.metadata