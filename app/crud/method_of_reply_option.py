from sqlalchemy.orm import Session
import uuid
from app.models.method_of_reply_option import MethodOfReplyOption

def get_method_of_reply(db: Session, id: uuid.UUID):
    return db.query(MethodOfReplyOption).filter(MethodOfReplyOption.id == id).first()

def get_methods_of_reply(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MethodOfReplyOption).offset(skip).limit(limit).all()

def create_method_of_reply(db: Session, label: str):
    db_obj = MethodOfReplyOption(id=uuid.uuid4(), label=label)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
