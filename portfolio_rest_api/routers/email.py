"""Handles email routes"""

from fastapi import APIRouter, status

from portfolio_rest_api.models import Email

router = APIRouter(
    prefix='/email',
    tags=['email']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def post_send_email(email: Email):  # pylint: disable=W0613
    """Handles email requests and forwards them to the configured email address"""
