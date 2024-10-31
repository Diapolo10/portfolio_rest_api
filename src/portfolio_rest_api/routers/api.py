"""Handle the entire backend API of the portfolio site."""

from fastapi import APIRouter

from portfolio_rest_api.routers.email import router as email_router

router = APIRouter(
    prefix='/api/v1',
    tags=['api'],
)

router.include_router(email_router)
