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
    notes = usecases.create_example_notes()

    return notes
