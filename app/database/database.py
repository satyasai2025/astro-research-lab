"""
Astro Research Lab
Database Manager

Initial Version:
- Creates SQLite database
- Creates required folders
- Provides SQLAlchemy Engine
- Provides Session Factory
"""

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.settings import DATABASE_PATH


# ==========================================================
# Ensure database folder exists
# ==========================================================

Path(DATABASE_PATH).parent.mkdir(
    parents=True,
    exist_ok=True,
)

# ==========================================================
# SQLAlchemy Base
# ==========================================================

Base = declarative_base()

# ==========================================================
# Engine
# ==========================================================

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

# ==========================================================
# Session Factory
# ==========================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# ==========================================================
# Database Manager
# ==========================================================

class DatabaseManager:
    """
    Handles database initialization
    and session creation.
    """

    @staticmethod
    def initialize() -> None:
        """
        Create all registered tables.
        """

        Base.metadata.create_all(bind=engine)

    @staticmethod
    def get_session():
        """
        Returns a new SQLAlchemy session.
        """

        return SessionLocal()

    @staticmethod
    def database_exists() -> bool:
        """
        Returns True if database file exists.
        """

        return DATABASE_PATH.exists()

    @staticmethod
    def database_location() -> Path:
        """
        Returns database file path.
        """

        return DATABASE_PATH