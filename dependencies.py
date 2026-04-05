from typing import Optional

from fastapi import Header, HTTPException, status

from app.models import UserRole


ROLE_ORDER = {
	UserRole.VIEWER: 1,
	UserRole.ANALYST: 2,
	UserRole.ADMIN: 3,
}


def _parse_role(role_header: Optional[str]) -> UserRole:
	if not role_header:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Missing X-Role header",
		)

	normalized = role_header.strip().lower()
	try:
		return UserRole(normalized)
	except ValueError as exc:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail="Invalid role. Use viewer, analyst, or admin",
		) from exc


def get_request_context(
	x_role: Optional[str] = Header(default=None, alias="X-Role"),
	x_user_id: Optional[int] = Header(default=None, alias="X-User-Id"),
) -> dict:
	"""Extract user context from request headers for simple role-based access."""
	role = _parse_role(x_role)
	return {"role": role, "user_id": x_user_id}


def require_viewer_or_above(
	x_role: Optional[str] = Header(default=None, alias="X-Role"),
) -> UserRole:
	return _parse_role(x_role)


def require_analyst_or_above(
	x_role: Optional[str] = Header(default=None, alias="X-Role"),
) -> UserRole:
	role = _parse_role(x_role)
	if ROLE_ORDER[role] < ROLE_ORDER[UserRole.ANALYST]:
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="Analyst or admin role required",
		)
	return role


def require_admin(
	x_role: Optional[str] = Header(default=None, alias="X-Role"),
) -> UserRole:
	role = _parse_role(x_role)
	if role != UserRole.ADMIN:
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="Admin role required",
		)
	return role
