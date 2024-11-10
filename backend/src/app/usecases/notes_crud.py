import datetime
from fastapi import HTTPException

__FAKE_DB_NOTES = {}

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


def check_token_existence(token: str):
    """
    Check if a token is in __FAKE_DB_NOTES
    """
    if token not in __FAKE_DB_NOTES:
        raise HTTPException(status_code=401, detail="Token not found")
