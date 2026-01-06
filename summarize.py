def summarize_text(text: str) -> str:
    """
    Simple extractive summary (deployment-safe)
    """
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) <= 2:
        return text

    return ". ".join(sentences[:2]) + "."
