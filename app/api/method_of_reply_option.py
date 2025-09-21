from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.crud.method_of_reply_option import get_methods_of_reply, get_method_of_reply, create_method_of_reply
from app.database import get_db
from app.schemas.method_of_reply_option import MethodOfReplyOption, MethodOfReplyOptionCreate
from app.auth.jwt import role_required
from app.models.user import UserRole

router = APIRouter()


@router.get("/", response_model=List[MethodOfReplyOption])
def read_methods_of_reply(skip: int = 0, limit: int = 100,
                          db: Session = Depends(get_db),
                          current_user: UserRole = Depends(role_required([UserRole.admin]))):
    return get_methods_of_reply(db, skip, limit)


@router.get("/{id}", response_model=MethodOfReplyOption)
def read_method_of_reply(id: UUID,
                         db: Session = Depends(get_db),
                         current_user: UserRole = Depends(role_required([UserRole.admin]))):
    obj = get_method_of_reply(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


@router.post("/", response_model=MethodOfReplyOption)
def create_method_of_reply_endpoint(obj_in: MethodOfReplyOptionCreate,
                                   db: Session = Depends(get_db),
                                   current_user: UserRole = Depends(role_required([UserRole.admin]))):
    return create_method_of_reply(db, label=obj_in.label)
