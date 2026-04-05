from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database stored in the project root folder.
DATABASE_URL = "sqlite:///./finance.db"

# check_same_thread is required for SQLite with FastAPI.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session factory for database operations.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models.
Base = declarative_base()


def get_db():
	"""Provide a transactional database session for each request."""
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
