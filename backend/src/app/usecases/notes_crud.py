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


def check_note_existence(token: str, note_id: int):
    """
    Check if a token has this specified note_id
    """
    tokennotes = __FAKE_DB_NOTES[token]
    if note_id < 0 or note_id >= len(tokennotes):
        raise HTTPException(status_code=404, detail="Note not found")


def create_note(token: str, note_data):
    """
    Create a new note
    """
    if token not in __FAKE_DB_NOTES:
        __FAKE_DB_NOTES[token] = []
    note_id = len(__FAKE_DB_NOTES[token])
    new_note = {
        "id": note_id,
        "session_id": 0,
        "content": note_data["content"],
        "latitude": note_data["latitude"],
        "longitude": note_data["longitude"],
        "creation_date": datetime.datetime.utcnow(),
        "updated_date": datetime.datetime.utcnow(),
    }
    __FAKE_DB_NOTES[token].append(new_note)
    return new_note


def read_notes(token: str):
    """
    read all notes of this specific token
    """
    check_token_existence(token)
    return __FAKE_DB_NOTES.get(token, [])


def read_note(token: str, note_id: int):
    """
    read a specific note of a specific token
    """
    check_token_existence(token)
    check_note_existence(token, note_id)
    return __FAKE_DB_NOTES[token][note_id]


def update_note(token: str, note_id, note_data):
    """
    update a specific note of a specific token
    """
    check_token_existence(token)
    check_note_existence(token, note_id)
    existing_note = __FAKE_DB_NOTES[token][note_id]
    existing_note["content"] = note_data.get("content", existing_note["content"])
    existing_note["latitude"] = note_data.get("latitude", existing_note["latitude"])
    existing_note["longitude"] = note_data.get("longitude", existing_note["longitude"])
    existing_note["updated_date"] = datetime.datetime.utcnow()
    return existing_note


def delete_note(token: str, note_id: int):
    """
    delete a specific note of a specific token
    """
    check_token_existence(token)
    check_note_existence(token, note_id)
    del __FAKE_DB_NOTES[token][note_id]
    return {"message": "Note deleted successfully"}
