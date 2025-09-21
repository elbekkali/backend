from sqlalchemy.orm import Session
import uuid
from app.models.call_type_query import CallTypeQuery

def get_call_type_query(db: Session, id: uuid.UUID):
    return db.query(CallTypeQuery).filter(CallTypeQuery.id == id).first()

def get_call_type_queries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CallTypeQuery).offset(skip).limit(limit).all()

def create_call_type_query(db: Session, label: str):
    db_obj = CallTypeQuery(id=uuid.uuid4(), label=label)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
