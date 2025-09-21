from sqlalchemy.orm import Session
import uuid
from app.models.response_status import ResponseStatus

def get_response_status(db: Session, id: uuid.UUID):
    return db.query(ResponseStatus).filter(ResponseStatus.id == id).first()

def get_response_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ResponseStatus).offset(skip).limit(limit).all()

def create_response_status(db: Session, label: str):
    db_obj = ResponseStatus(id=uuid.uuid4(), label=label)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
