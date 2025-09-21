from sqlalchemy.orm import Session
import uuid
from app.models.call import Call
from app.schemas.call import CallCreate, CallUpdate
from app.models.call import CallStatus


def get_call(db: Session, call_id: uuid.UUID):
    return db.query(Call).filter(Call.id == call_id).first()


def get_calls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Call).offset(skip).limit(limit).all()



def create_call(db: Session, call: CallCreate):
    # Convertir status string en Enum, si besoin
    if isinstance(call.status, str):
        status_enum = CallStatus(call.status.capitalize())
    else:
        status_enum = call.status

    db_call = Call(
        id=uuid.uuid4(),
        date=call.date,
        time=call.time,
        recieved_from=call.recieved_from,
        client_name=call.client_name,
        contact_number=call.contact_number,
        type_of_query_id=call.type_of_query_id,
        reason_of_call=call.reason_of_call,
        answered_by=call.answered_by,
        replied_to_id=call.replied_to_id,
        replied_method_id=call.replied_method_id,
        replied_by=call.replied_by,
        assigned_to_id=call.assigned_to_id,
        action_to_be_taken_by=call.action_to_be_taken_by,
        actions_to_be_taken=call.actions_to_be_taken,
        action_taken=call.action_taken,
        other_comments=call.other_comments,
        status=status_enum,
    )
    db.add(db_call)
    db.commit()
    db.refresh(db_call)
    return db_call



def update_call(db: Session, call_id: uuid.UUID, call_update: CallUpdate):
    db_call = get_call(db, call_id)
    if not db_call:
        return None
    update_data = call_update.dict(exclude_unset=True)

    if "status" in update_data:
        if isinstance(update_data["status"], str):
            update_data["status"] = CallStatus(update_data["status"].capitalize())

    for key, value in update_data.items():
        setattr(db_call, key, value)
    db.commit()
    db.refresh(db_call)
    return db_call



def delete_call(db: Session, call_id: uuid.UUID):
    db_call = get_call(db, call_id)
    if not db_call:
        return None
    db.delete(db_call)
    db.commit()
    return db_call
