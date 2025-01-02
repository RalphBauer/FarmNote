from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import notes_router, sessions_router
from .database import engine, Base

# Erstelle die Tabellen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FarmNote",
    summary="Http API for the App FarmNote",
    version="1.0.1",
    contact={
        "name": "Your Name (Developer)",
        "url": "https://git.fhwn.ac.at/your-repository/",
        "email": "yourmail@fhwn.ac.at"
    },
    root_path=settings.root_path,
    openapi_tags=[
        {
            "name": "notes",
            "description": "Manage notes",
        },
        {
            "name": "sessions",
            "description": "Manage sessions and tokens",
        }
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes_router)
app.include_router(sessions_router)
