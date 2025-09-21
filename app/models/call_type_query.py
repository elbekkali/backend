from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from . import Base


class CallTypeQuery(Base):
    __tablename__ = "call_type_queries"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    label = Column(String(100), unique=True, nullable=False)
