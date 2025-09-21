from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from . import Base


class ResponseStatus(Base):
    __tablename__ = "response_status"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    label = Column(String(50), unique=True, nullable=False)
