from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil, os

from transcribe import transcribe_audio
from summarize import summarize_text
from actions import extract_action_items
from dates import detect_due_dates
from database import save_note, get_notes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    transcription = transcribe_audio(path)
    summary = summarize_text(transcription)

    actions = extract_action_items(transcription)
    actions_with_dates = detect_due_dates(actions)

    save_note(transcription, summary, actions_with_dates)

    return {
        "transcription": transcription,
        "summary": summary,
        "actions": actions_with_dates
    }

@app.get("/history/")
def history():
    return get_notes()


import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
