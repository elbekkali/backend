from sqlalchemy.orm import Session
from app.models.user import User, UserStatus
from app.schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.logging_config import logger


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        logger.warning(f"Attempt to create duplicate email: {user.email}")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    hashed_password = hash_password(user.password)
    db_user = User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        password_hash=hashed_password,
        phone_number=user.phone_number,
        role=user.role,
        status=user.status,
        birth_date=user.birth_date,
        address=user.address,
        profile_picture=user.profile_picture,
        notes=user.notes,
    )
    db.add(db_user)
    try:
        db.commit()
        logger.info(f"User created: {user.email}")
    except IntegrityError:
        db.rollback()
        logger.error(f"IntegrityError when creating user with email: {user.email}")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 10, include_inactive: bool = False):
    query = db.query(User)
    if not include_inactive:
        query = query.filter(User.status == UserStatus.active)
    return query.offset(skip).limit(limit).all()


def get_user_by_email_exclude_user(db: Session, email: str, user_id: str):
    return db.query(User).filter(User.email == email, User.id != user_id).first()


def update_user(db: Session, user_id: str, user_update: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        logger.warning(f"User update failed, user not found: {user_id}")
        return None

    update_data = user_update.dict(exclude_unset=True)

    if "email" in update_data:
        existing_user = get_user_by_email_exclude_user(db, update_data["email"], user_id)
        if existing_user:
            logger.warning(f"User update failed, email already used: {update_data['email']}")
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered by another user")

    if "password" in update_data:
        db_user.password_hash = hash_password(update_data.pop("password"))

    for key, value in update_data.items():
        setattr(db_user, key, value)
    try:
        db.commit()
        logger.info(f"User updated: {user_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error updating user {user_id}: {e}")
        raise e
    db.refresh(db_user)
    return db_user


def deactivate_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        logger.warning(f"User deactivate failed, user not found: {user_id}")
        return None
    if db_user.status == UserStatus.inactive:
        return db_user  # déjà inactif
    db_user.status = UserStatus.inactive
    try:
        db.commit()
        logger.info(f"User deactivated: {user_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error deactivating user {user_id}: {e}")
        raise e
    db.refresh(db_user)
    return db_user


def activate_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        logger.warning(f"User activate failed, user not found: {user_id}")
        return None
    if db_user.status == UserStatus.active:
        return db_user  # déjà actif
    db_user.status = UserStatus.active
    try:
        db.commit()
        logger.info(f"User activated: {user_id}")
    except Exception as e:
        db.rollback()
        logger.error(f"Error activating user {user_id}: {e}")
        raise e
    db.refresh(db_user)
    return db_user
