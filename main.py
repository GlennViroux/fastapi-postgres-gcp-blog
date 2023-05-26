from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from database import init_db
from models import Note

app = FastAPI(title="fastapi-gcp")
init_db(app)


@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>All good!</h2>"


class CreateNotePayload(BaseModel):
    filename: str
    title: str
    content: str


@app.post("/notes")
async def create_note(payload: CreateNotePayload):
    note = await Note.create(**payload.dict())
    return {"message": f"Note created successfully with id {note.id}"}


@app.get("/notes/{title}")
async def get_note_by_title(title: str):
    if not (note := await Note.get_or_none(title=title)):
        raise HTTPException(status_code=404, detail="Note not found")

    return note.id
