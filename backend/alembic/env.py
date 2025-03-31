from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bitly", "db")))

from backend.bitly.db.engine import Base  # Import Base from bitly/db/engine.py
from backend.bitly.db.models import *  # Import models

# Alembic Configuration
config = context.config
fileConfig(config.config_file_name)

# Set the target metadata for Alembic to generate migrations
target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/bitly_db")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
