from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    email: str

class UserLogin(BaseModel):
    email: str
    password: str
