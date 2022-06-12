from pydantic import BaseModel

class Email(BaseModel):
    name: str
    email: str
    subject: str
    message: str
