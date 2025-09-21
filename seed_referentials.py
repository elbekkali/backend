import uuid
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.call_type_query import CallTypeQuery
from app.models.method_of_reply_option import MethodOfReplyOption
from app.models.response_status import ResponseStatus

# Listes à insérer
method_of_reply_options = [
    "Whatsapp Call",
    "Whatsapp Msg",
    "Ringover",
    "Fix",
    "Mail",
    "Directly at agency",
    "Other",
]

type_queries = [
    "New ticket",
    "Existing ticket",
    "Modification",
    "Cancellation",
    "Refund",
    "Schedule change",
    "Payment",
    "Insurance",
    "Visa",
    "OCI",
    "Passport Renewal",
    "Special Request",
    "Wheel Chair",
    "Other",
    "Omra",
]

response_statuses = [
    "Yes",
    "No",
    "Pending",
    "Cancelled",
]

def seed_table(db: Session, model, data_list):
    for label in data_list:
        exists = db.query(model).filter(model.label == label).first()
        if not exists:
            item = model(id=uuid.uuid4(), label=label)
            db.add(item)
    db.commit()

def main():
    db = SessionLocal()
    try:
        seed_table(db, MethodOfReplyOption, method_of_reply_options)
        seed_table(db, CallTypeQuery, type_queries)
        seed_table(db, ResponseStatus, response_statuses)
        print("Données référentielles insérées avec succès.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
