from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class NoteBase(BaseModel):
    """
    Base schema for a note
    """
    content: str
    latitude: float
    longitude: float


class Note(NoteBase):
    """
    Schema of a note
    """
    id: int
    session_id: int
    creation_date: datetime
    updated_date: datetime


class NoteCreate(NoteBase):
    """
    Schema for creating a new note
    """
    pass


class NoteUpdate(NoteBase):
    """
    Schema for updating an existing note
    """
    content: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
