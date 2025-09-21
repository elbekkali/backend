from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.schemas.user import UserCreate, UserRead, UserUpdate, UserReplace
from app.crud.user import create_user, get_users, get_user, update_user, activate_user, deactivate_user
from app.database import get_db
from sqlalchemy.exc import SQLAlchemyError
from app.logging_config import logger
from app.auth.jwt import get_current_user
from app.models.user import User, UserRole, UserStatus

router = APIRouter()

@router.get("/users/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/users/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user_route(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        db_user = create_user(db=db, user=user)
        logger.info(f"User created: {db_user.email}")
        return db_user
    except HTTPException as e:
        logger.warning(f"User creation failed: {e.detail}")
        raise e
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")

@router.get("/users/", response_model=List[UserRead])
def read_users(
    skip: int = 0,
    limit: int = 10,
    include_inactive: bool = Query(False),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        users = get_users(db=db, skip=skip, limit=limit, include_inactive=include_inactive)
        logger.info(f"Read users by {current_user.email}, include_inactive={include_inactive}, count={len(users)}")
        return users
    except SQLAlchemyError as e:
        logger.error(f"Database error: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.get("/agents/active", response_model=List[UserRead])
def read_active_agents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        agents = db.query(User).filter(
            User.role == UserRole.agent,
            User.status == UserStatus.active
        ).all()
        return agents
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erreur serveur")

@router.put("/users/{user_id}", response_model=UserRead)
def update_user_route(user_id: UUID, user: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        updated_user = update_user(db, user_id, user)
        if not updated_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return updated_user
    except HTTPException as e:
        raise e
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")

@router.patch("/users/{user_id}", response_model=UserRead)
def partial_update_user(user_id: UUID, user_update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        updated_user = update_user(db, user_id, user_update)
        if not updated_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return updated_user
    except HTTPException as e:
        raise e
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Database error")

@router.patch("/users/{user_id}/deactivate", response_model=UserRead)
def deactivate_user_route(user_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = deactivate_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found or already deactivated")
    return user

@router.patch("/users/{user_id}/activate", response_model=UserRead)
def activate_user_route(user_id: UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = activate_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found or already activated")
    return user
