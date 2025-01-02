from sqlalchemy.orm import Session
from fastapi import HTTPException
import random
import string
from ..models.models import User


def create_token(db: Session, length=6):
    if length != 6:
        raise ValueError("The length of the token must be 6")

    characters = string.ascii_uppercase
    token = ''.join(random.choice(characters) for _ in range(length))

    # Speichern des Tokens in der Datenbank
    new_user = User(token=token)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return token


def check_token_existence(db: Session, token: str):
    if not db.query(User).filter(User.token == token).first():
        raise HTTPException(status_code=401, detail="Token not found")



def load_session(db: Session, token: str):
    user = db.query(User).filter(User.token == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Token not found")

    # Hier können Sie die gewünschten Sitzungsdaten zurückgeben
    return {
        "session_id": str(user.session_id),  # Konvertieren Sie die session_id in einen String
        "token": user.token,
        # Fügen Sie hier weitere relevante Daten hinzu
    }
