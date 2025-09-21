from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.schemas.call import CallCreate, CallUpdate, Call
from app.crud.call import get_call, get_calls, create_call, update_call, delete_call
from app.database import get_db
from app.auth.jwt import get_current_user
from app.models.user import User

router = APIRouter()

@router.get("/", response_model=List[Call])
def read_calls(skip: int = 0, limit: int = 100,
               db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    return get_calls(db, skip=skip, limit=limit)

@router.get("/{call_id}", response_model=Call)
def read_call(call_id: UUID,
              db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):
    db_call = get_call(db, call_id)
    if not db_call:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call

@router.post("/", response_model=Call, status_code=status.HTTP_201_CREATED)
def create_call_endpoint(call_in: CallCreate,
                        db: Session = Depends(get_db)):
    return create_call(db, call_in)

@router.put("/{call_id}", response_model=Call)
def update_call_endpoint(call_id: UUID,
                         call_in: CallUpdate,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    db_call = update_call(db, call_id, call_in)
    if not db_call:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call

@router.delete("/{call_id}", response_model=Call)
def delete_call_endpoint(call_id: UUID,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(get_current_user)):
    db_call = delete_call(db, call_id)
    if not db_call:
        raise HTTPException(status_code=404, detail="Call not found")
    return db_call
