from pydantic import BaseModel
from uuid import UUID


class CallTypeQueryBase(BaseModel):
    label: str


class CallTypeQueryCreate(CallTypeQueryBase):
    pass


class CallTypeQueryInDBBase(CallTypeQueryBase):
    id: UUID

    class Config:
        from_attributes = True


class CallTypeQuery(CallTypeQueryInDBBase):
    pass
