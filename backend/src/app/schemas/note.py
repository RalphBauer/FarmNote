from datetime import datetime

from pydantic import BaseModel


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
