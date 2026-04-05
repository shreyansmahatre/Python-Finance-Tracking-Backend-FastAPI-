import enum

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import relationship

from app.database import Base


class UserRole(str, enum.Enum):
	VIEWER = "viewer"
	ANALYST = "analyst"
	ADMIN = "admin"


class TransactionType(str, enum.Enum):
	INCOME = "income"
	EXPENSE = "expense"


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(100), nullable=False)
	email = Column(String(255), unique=True, nullable=False, index=True)
	role = Column(Enum(UserRole), nullable=False, default=UserRole.VIEWER)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

	transactions = relationship("Transaction", back_populates="user", cascade="all, delete-orphan")


class Transaction(Base):
	__tablename__ = "transactions"

	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
	amount = Column(Numeric(12, 2), nullable=False)
	type = Column(Enum(TransactionType), nullable=False, index=True)
	category = Column(String(100), nullable=False, index=True)
	date = Column(Date, nullable=False, index=True)
	notes = Column(Text, nullable=True)
	created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
	updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

	user = relationship("User", back_populates="transactions")
