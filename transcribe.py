import whisper

# Load the smallest model for low-memory servers
model = whisper.load_model("tiny")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe audio using Whisper
    """
    result = model.transcribe(file_path, fp16=False)
    return result["text"]
