from transformers import pipeline

# 🔥 FAST summarizer
summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

def summarize_text(text: str) -> str:
    if len(text.split()) < 25:
        return text  # skip summarization for short text

    summary = summarizer(
        text,
        max_length=80,
        min_length=25,
        do_sample=False
    )

    return summary[0]["summary_text"]
