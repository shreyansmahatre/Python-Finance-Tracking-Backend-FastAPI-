from fastapi import FastAPI

from app.database import Base, engine
from app.routers.summary import router as summary_router
from app.routers.transactions import router as transactions_router
from app.routers.users import router as users_router

# Import models so SQLAlchemy can detect them before create_all.
from app import models  # noqa: F401

app = FastAPI(title="Finance Tracker API", version="1.0.0")

app.include_router(transactions_router)
app.include_router(summary_router)
app.include_router(users_router)


@app.on_event("startup")
def on_startup() -> None:
	"""Create database tables when the application starts."""
	Base.metadata.create_all(bind=engine)


@app.get("/")
def health_check() -> dict:
	return {"status": "ok", "message": "Finance Tracker API is running"}
