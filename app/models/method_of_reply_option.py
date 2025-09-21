from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from . import Base


class MethodOfReplyOption(Base):
    __tablename__ = "method_of_reply_options"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    label = Column(String(100), unique=True, nullable=False)
