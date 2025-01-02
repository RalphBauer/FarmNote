from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.models import Note
from datetime import datetime
from .sessions_crud import check_token_existence

def create_note(db: Session, token: str, note_data):
    if note_data["field_id"] < 0:
        raise HTTPException(status_code=422, detail="field_id should not be less than zero.")
    if note_data["latitude"] < 0:
        raise HTTPException(status_code=422, detail="latitude should not be less than zero.")
    if note_data["longitude"] < 0:
        raise HTTPException(status_code=422, detail="longitude should not be less than zero.")

    new_note = Note(
        content=note_data["content"],
        latitude=note_data["latitude"],
        longitude=note_data["longitude"],
        field_id=note_data["field_id"],
        session_id=0,  # Hier könnte eine Logik zur Bestimmung der session_id erforderlich sein
        token=token,
        creation_date=datetime.utcnow(),
        updated_date=datetime.utcnow(),
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

def read_notes(db: Session, token: str):
    check_token_existence(db, token)
    return db.query(Note).filter(Note.token == token).all()

def read_note(db: Session, token: str, note_id: int):
    check_token_existence(db, token)
    note = db.query(Note).filter(Note.token == token, Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

def update_note(db: Session, token: str, note_id: int, note_data):
    check_token_existence(db, token)
    note = db.query(Note).filter(Note.token == token, Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note.content = note_data.get("content", note.content)
    note.latitude = note_data.get("latitude", note.latitude)
    note.longitude = note_data.get("longitude", note.longitude)
    note.field_id = note_data.get("field_id", note.field_id)
    note.updated_date = datetime.utcnow()

    db.commit()
    return note

def delete_note(db: Session, token: str, note_id: int):
    check_token_existence(db, token)
    note = db.query(Note).filter(Note.token == token, Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
