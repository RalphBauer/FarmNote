from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'user'

    session_id = Column(Integer, primary_key=True)
    token = Column(String, unique=True, nullable=False)

    # Beziehung zu Notizen, unter Angabe des Foreign Keys
    notes = relationship("Note", back_populates="user", foreign_keys="Note.token")

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    field_id = Column(Integer, nullable=False)
    session_id = Column(Integer, ForeignKey('user.session_id'), nullable=False)
    token = Column(String(6), ForeignKey('user.token'), nullable=False)
    creation_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Beziehung zu User, unter Angabe des Foreign Keys
    user = relationship("User", back_populates="notes", foreign_keys=[token])

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'field_id': self.field_id,
            'session_id': self.session_id,
            'token': self.token,
            'creation_date': self.creation_date.isoformat(),
            'updated_date': self.updated_date.isoformat()
        }
