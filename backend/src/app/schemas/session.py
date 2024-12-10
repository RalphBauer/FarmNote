from pydantic import BaseModel

class SessionResponse(BaseModel):
    session_id: str  # session_id als String
    token: str       # Token als String
