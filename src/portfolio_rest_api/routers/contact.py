"""Handle email routes."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, status

if TYPE_CHECKING:
    from portfolio_rest_api.models import Email

router = APIRouter(
    prefix='/contact',
    tags=['contact'],
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_send_email(email: Email) -> Email:
    """Handle email requests and forward them to the configured email address."""
    return email  # NOTE: Make this do stuff
