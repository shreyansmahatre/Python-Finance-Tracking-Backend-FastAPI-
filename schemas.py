from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from app.models import TransactionType, UserRole


class UserCreate(BaseModel):
	name: str = Field(min_length=2, max_length=100)
	email: EmailStr
	role: UserRole = UserRole.VIEWER


class UserOut(BaseModel):
	id: int
	name: str
	email: EmailStr
	role: UserRole
	created_at: datetime

	model_config = ConfigDict(from_attributes=True)


class TransactionCreate(BaseModel):
	user_id: int
	amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
	type: TransactionType
	category: str = Field(min_length=1, max_length=100)
	date: date
	notes: Optional[str] = Field(default=None, max_length=500)

	@field_validator("category")
	@classmethod
	def normalize_category(cls, value: str) -> str:
		cleaned = value.strip()
		if not cleaned:
			raise ValueError("Category must not be empty")
		return cleaned


class TransactionUpdate(BaseModel):
	amount: Optional[Decimal] = Field(default=None, gt=0, max_digits=12, decimal_places=2)
	type: Optional[TransactionType] = None
	category: Optional[str] = Field(default=None, min_length=1, max_length=100)
	date: Optional[date] = None
	notes: Optional[str] = Field(default=None, max_length=500)

	@field_validator("category")
	@classmethod
	def normalize_optional_category(cls, value: Optional[str]) -> Optional[str]:
		if value is None:
			return value
		cleaned = value.strip()
		if not cleaned:
			raise ValueError("Category must not be empty")
		return cleaned


class TransactionOut(BaseModel):
	id: int
	user_id: int
	amount: Decimal
	type: TransactionType
	category: str
	date: date
	notes: Optional[str]
	created_at: datetime
	updated_at: datetime

	model_config = ConfigDict(from_attributes=True)


class SummaryOverviewOut(BaseModel):
	total_income: Decimal
	total_expenses: Decimal
	current_balance: Decimal


class CategorySummaryOut(BaseModel):
	category: str
	total: Decimal


class MonthlySummaryOut(BaseModel):
	month: str
	total_income: Decimal
	total_expenses: Decimal
	balance: Decimal
