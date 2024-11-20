from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .routers import notes_router


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
        }
    ],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_origin_regex="^http://(127\.0\.0\.1|localhost)(:\d+)?.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes_router)
