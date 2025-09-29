# backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL
import os

# Activer echo uniquement en développement
echo_mode = os.getenv("ENVIRONMENT", "development") == "development"

engine = create_engine(DATABASE_URL, echo=echo_mode)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dépendance FastAPI pour récupérer une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()