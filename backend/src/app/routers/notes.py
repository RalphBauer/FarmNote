import datetime
from typing import List

from fastapi import APIRouter, Depends

from .. import schemas, dependencies, usecases

router = APIRouter(
    prefix='/notes',
    tags=['notes'],
)


@router.get("/",
                response_model=List[schemas.Note],
                operation_id='readNotes',
                description='''
                    Return all note of an existing session.
                ''',
                responses={
                },
            )
def read_notes(token: str = Depends(dependencies.get_session_token)):
    notes = usecases.notes_crud.read_notes(token)

    return notes


@router.post("/",
             response_model=schemas.Note,
             operation_id='createNote',
             description='''
                 Create a new note for the session.
             ''',
             responses={
                 201: {"description": "Note created successfully"},
                 400: {"description": "Invalid input"},
             },
             )
def create_note(note_data: schemas.note.NoteCreate, token: str = Depends(dependencies.get_session_token)):
    return usecases.notes_crud.create_note(token, note_data.dict())
