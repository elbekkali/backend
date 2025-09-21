# backend/app/models/__init__.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Importez les modèles ici pour Alembic
from .user import User
# Ajoutez autres modèles progressivement
from .call import Call
from .call_type_query import CallTypeQuery
from .method_of_reply_option import MethodOfReplyOption
from .response_status import ResponseStatus
# autres modèles existants…
