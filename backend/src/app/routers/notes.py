import datetime
from typing import List
from fastapi import APIRouter, Depends
from .. import schemas, dependencies, usecases
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix='/notes',
    tags=['notes'],
)

@router.get("/", response_model=List[schemas.Note])
def read_notes(token: str = Depends(dependencies.get_session_token), db: Session = Depends(get_db)):
    notes = usecases.notes_crud.read_notes(db, token)
    return notes

@router.post("/", response_model=schemas.Note)
def create_note(note_data: schemas.NoteCreate, token: str = Depends(dependencies.get_session_token), db: Session = Depends(get_db)):
    return usecases.notes_crud.create_note(db, token, note_data.dict())

@router.get("/{note_id}", response_model=schemas.Note)
def read_note(note_id: int, token: str = Depends(dependencies.get_session_token), db: Session = Depends(get_db)):
    return usecases.notes_crud.read_note(db, token, note_id)

@router.put("/{note_id}", response_model=schemas.Note)
def update_note(note_id: int, note_data: schemas.NoteUpdate, token: str = Depends(dependencies.get_session_token), db: Session = Depends(get_db)):
    return usecases.notes_crud.update_note(db, token, note_id, note_data.dict())

@router.delete("/{note_id}", response_model=dict)
def delete_note(note_id: int, token: str = Depends(dependencies.get_session_token), db: Session = Depends(get_db)):
    return usecases.notes_crud.delete_note(db, token, note_id)
