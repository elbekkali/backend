from pydantic import BaseModel
from uuid import UUID


class ResponseStatusBase(BaseModel):
    label: str


class ResponseStatusCreate(ResponseStatusBase):
    pass


class ResponseStatusInDBBase(ResponseStatusBase):
    id: UUID

    class Config:
        from_attributes = True


class ResponseStatus(ResponseStatusInDBBase):
    pass
