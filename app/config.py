from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables depuis .env situé à la racine

SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))  # Ajout avec valeur par défaut
ALGORITHM = os.getenv("ALGORITHM", "HS256")  # Ajout avec valeur par défaut (HS256 est un algorithme courant pour JWT)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")