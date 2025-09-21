from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.api import user, auth, call, call_type_query, method_of_reply_option, response_status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # Origines autorisées
    allow_credentials=True,
    allow_methods=["*"],            # Toutes méthodes HTTP autorisées
    allow_headers=["*"],            # Tous headers autorisés
)

app.include_router(user.router, tags=["users"])
app.include_router(auth.router, tags=["auth"])
app.include_router(call.router, prefix="/calls", tags=["calls"])
app.include_router(call_type_query.router, prefix="/call-type-queries", tags=["call_type_queries"])
app.include_router(method_of_reply_option.router, prefix="/method-of-reply-options", tags=["method_of_reply_options"])
app.include_router(response_status.router, prefix="/response-statuses", tags=["response_statuses"])

@app.get("/")
def test_connection(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1")).scalar()
    return {"database_status": result}
