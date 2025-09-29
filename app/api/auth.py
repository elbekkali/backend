from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.auth.jwt import authenticate_user, create_access_token, create_refresh_token, validate_refresh_token
from app.database import get_db
from app.models.user import User
from datetime import timedelta

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou mot de passe incorrect")
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    refresh_token = create_refresh_token(db, user.id)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh-token", description="Rafraîchit un token d'accès à partir d'un refresh token valide")
async def refresh_access_token(refresh_token: str, db: Session = Depends(get_db)):
    refresh_token_obj = validate_refresh_token(db, refresh_token)
    if not refresh_token_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token invalide ou expiré")
    
    user = db.query(User).filter(User.id == refresh_token_obj.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Utilisateur non trouvé")
    
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }