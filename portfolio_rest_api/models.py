"""Contains Pydantic models"""

from pydantic import BaseModel  # pylint: disable=E0611


class Email(BaseModel):  # pylint: disable=R0903
    """Models emails"""

    name: str
    email: str
    subject: str
    message: str
