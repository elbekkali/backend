from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.crud.call_type_query import get_call_type_queries, get_call_type_query, create_call_type_query
from app.database import get_db
from app.schemas.call_type_query import CallTypeQuery, CallTypeQueryCreate
from app.auth.jwt import role_required
from app.models.user import UserRole

router = APIRouter()


@router.get("/", response_model=List[CallTypeQuery])
def read_call_type_queries(skip: int = 0, limit: int = 100,
                           db: Session = Depends(get_db),
                           current_user: UserRole = Depends(role_required([UserRole.admin]))):
    return get_call_type_queries(db, skip, limit)


@router.get("/{id}", response_model=CallTypeQuery)
def read_call_type_query(id: UUID,
                         db: Session = Depends(get_db),
                         current_user: UserRole = Depends(role_required([UserRole.admin]))):
    db_obj = get_call_type_query(db, id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not found")
    return db_obj


@router.post("/", response_model=CallTypeQuery)
def create_call_type_query_endpoint(obj_in: CallTypeQueryCreate,
                                   db: Session = Depends(get_db),
                                   current_user: UserRole = Depends(role_required([UserRole.admin]))):
    return create_call_type_query(db, label=obj_in.label)
