from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.crud.response_status import get_response_statuses, get_response_status, create_response_status
from app.database import get_db
from app.schemas.response_status import ResponseStatus, ResponseStatusCreate
from app.auth.jwt import role_required
from app.models.user import UserRole

router = APIRouter()


@router.get("/", response_model=List[ResponseStatus])
def read_response_statuses(skip: int = 0, limit: int = 100,
                           db: Session = Depends(get_db),
                           current_user: UserRole = Depends(role_required([UserRole.admin]))):
    return get_response_statuses(db, skip, limit)


@router.get("/{id}", response_model=ResponseStatus)
def read_response_status(id: UUID,
                         db: Session = Depends(get_db),
                         current_user: UserRole = Depends(role_required([UserRole.admin]))):
    obj = get_response_status(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@router.post("/", response_model=ResponseStatus)
def create_response_status_endpoint(obj_in: ResponseStatusCreate,
                                   db: Session = Depends(get_db),
                                   current_user: UserRole = Depends(role_required([UserRole.admin]))):
    return create_response_status(db, label=obj_in.label)
