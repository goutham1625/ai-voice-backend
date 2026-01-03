import whisper
import os

# Make sure ffmpeg is visible
os.environ["PATH"] += os.pathsep + r"D:\AI\ffmpeg-8.0.1-essentials_build\bin"

# 🔥 FAST MODEL
model = whisper.load_model("tiny")

def transcribe_audio(file_path: str) -> str:
    result = model.transcribe(file_path, fp16=False)
    return result["text"]
