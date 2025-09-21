from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date as DateType, time as TimeType
from enum import Enum

class CallStatus(str, Enum):
    closed = "Closed"
    pending = "Pending"
    open = "Open"

class CallBase(BaseModel):
    date: DateType
    time: TimeType
    recieved_from: Optional[str] = None
    client_name: str
    contact_number: str
    type_of_query_id: UUID
    reason_of_call: str
    answered_by: str
    replied_to_id: UUID
    replied_method_id: UUID
    replied_by: str
    assigned_to_id: Optional[UUID] = None
    action_to_be_taken_by: Optional[str] = None
    actions_to_be_taken: Optional[str] = None
    action_taken: Optional[str] = None
    other_comments: Optional[str] = None
    status: CallStatus = CallStatus.pending

class CallCreate(CallBase):
    pass

class CallUpdate(BaseModel):
    date: Optional[DateType] = None
    time: Optional[TimeType] = None
    recieved_from: Optional[str] = None
    client_name: Optional[str] = None
    contact_number: Optional[str] = None
    type_of_query_id: Optional[UUID] = None
    reason_of_call: Optional[str] = None
    answered_by: Optional[str] = None
    replied_to_id: Optional[UUID] = None
    replied_method_id: Optional[UUID] = None
    replied_by: Optional[str] = None
    assigned_to_id: Optional[UUID] = None
    action_to_be_taken_by: Optional[str] = None
    actions_to_be_taken: Optional[str] = None
    action_taken: Optional[str] = None
    other_comments: Optional[str] = None
    status: Optional[CallStatus] = None

class CallInDBBase(CallBase):
    id: UUID

    class Config:
        from_attributes = True

class Call(CallInDBBase):
    pass
