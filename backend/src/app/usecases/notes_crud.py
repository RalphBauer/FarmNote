import datetime
from fastapi import HTTPException

def create_example_notes():
    """
    Return a list of example notes for testing purposes
    """
    notes = [
        {
            "id": 0,
            "session_id": 0,
            "content": 'Hello World',
            "latitude": 48.1271,
            "longitude": 15.1247,
            "creation_date": datetime.datetime.utcnow(),
            "updated_date": datetime.datetime.utcnow(),
        },
        {
            "id": 1,
            "session_id": 0,
            "content": 'Example Note 2',
            "latitude": 48.21,
            "longitude": 15.125,
            "creation_date": datetime.datetime.utcnow(),
            "updated_date": datetime.datetime.utcnow(),
        }
    ]

    return notes
