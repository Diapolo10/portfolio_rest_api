"""Portfolio site REST API."""

import logging
import os
from pathlib import Path

import uvicorn
from dotenv import dotenv_values
from fastapi import BackgroundTasks, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema

from portfolio_rest_api.logger import ROOT_LOGGER_NAME, setup_logging
from portfolio_rest_api.routers.api import router as api_router

logger = logging.getLogger(ROOT_LOGGER_NAME)
setup_logging()

PROJECT_DIR = Path(__file__).parent.parent.parent
ENV_FILE = PROJECT_DIR / '.env'

DEFAULT_CONFIG = {
    'HOST': '127.0.0.1',
    'PORT': 8080,
}

config = {
    **DEFAULT_CONFIG,
    **dotenv_values(),  # ENV_FILE),
    **os.environ,
}

app = FastAPI()

app.include_router(api_router)

origins = [
    "http://diapolo10.github.io/",
    "https://diapolo10.github.io/",
    "http://localhost",
    "http://localhost:8080",
]

email_config = ConnectionConfig(
    MAIL_USERNAME=config['MAIL_USERNAME'],
    MAIL_PASSWORD=config['MAIL_PASSWORD'],
    MAIL_FROM=config['MAIL_FROM'],
    MAIL_PORT=config['MAIL_PORT'],
    MAIL_SERVER=config['MAIL_SERVER'],
    MAIL_FROM_NAME=config['MAIL_FROM_NAME'],
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER='./templates/email',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=["*"],
)


async def send_email_async(subject: str, email_to: str, body: dict) -> None:
    """Send emails asynchronously."""
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )

    fastmail = FastMail(email_config)

    await fastmail.send_message(message, template_name='email.html')


def send_email_background(background_tasks: BackgroundTasks, subject: str, email_to: str, body: dict) -> None:
    """Background task for sending emails."""
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        body=body,
        subtype='html',
    )
    fastmail = FastMail(email_config)
    background_tasks.add_task(
       fastmail.send_message, message, template_name='email.html',
    )


if __name__ == '__main__':
    uvicorn.run('main:app', host=config['HOST'], port=config['PORT'], reload=True)
