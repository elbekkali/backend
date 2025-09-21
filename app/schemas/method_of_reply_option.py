from pydantic import BaseModel
from uuid import UUID


class MethodOfReplyOptionBase(BaseModel):
    label: str


class MethodOfReplyOptionCreate(MethodOfReplyOptionBase):
    pass


class MethodOfReplyOptionInDBBase(MethodOfReplyOptionBase):
    id: UUID

    class Config:
        from_attributes = True


class MethodOfReplyOption(MethodOfReplyOptionInDBBase):
    pass
