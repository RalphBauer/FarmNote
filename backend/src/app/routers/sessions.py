# Datei: backend/src/app/routers/sessions.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import usecases
from ..database import get_db
from typing import Dict
from ..schemas.session import SessionResponse  # Importieren Sie das SessionResponse-Schema

router = APIRouter(
    prefix='/sessions',
    tags=['sessions'],
)

@router.post("/create-token/", response_model=Dict[str, str])
def create_token(length: int = 6, db: Session = Depends(get_db)):
    token = usecases.sessions_crud.create_token(db, length)
    return {"token": token}

@router.post("/create-session/", response_model=Dict[str, str])
def create_session(length: int = 6, db: Session = Depends(get_db)):
    token = usecases.sessions_crud.create_token(db, length)
    print(token)
    print(type(token))
    print("hallo")
    return {"token": token}

@router.get("/load-session/", response_model=SessionResponse)  # Verwenden Sie das neue Schema
def load_session(token: str, db: Session = Depends(get_db)):
    session_data = usecases.sessions_crud.load_session(db, token)
    return session_data
