from sqlalchemy import Column, String, Date, Time, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from . import Base
import uuid
import enum
from datetime import datetime


class CallStatus(enum.Enum):
    closed = "Closed"
    pending = "Pending"
    open = "Open"


class Call(Base):
    __tablename__ = "calls"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    recieved_from = Column(String, nullable=True)
    client_name = Column(String, nullable=False)
    contact_number = Column(String, nullable=False)

    type_of_query_id = Column(UUID(as_uuid=True), ForeignKey("call_type_queries.id"), nullable=False)
    reason_of_call = Column(String, nullable=False)

    answered_by = Column(String, nullable=False)
    replied_to_id = Column(UUID(as_uuid=True), ForeignKey("response_status.id"), nullable=False)
    replied_method_id = Column(UUID(as_uuid=True), ForeignKey("method_of_reply_options.id"), nullable=False)
    replied_by = Column(String, nullable=False)

    assigned_to_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    # Voici la ligne à ajouter !
    action_to_be_taken_by = Column(String, nullable=True)

    actions_to_be_taken = Column(String, nullable=True)
    action_taken = Column(String, nullable=True)
    other_comments = Column(String, nullable=True)

    status = Column(Enum(CallStatus), default=CallStatus.pending, nullable=False)

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relations avec ORM
    type_of_query = relationship("CallTypeQuery")
    replied_to = relationship("ResponseStatus")
    replied_method = relationship("MethodOfReplyOption")
    assigned_to = relationship("User")

