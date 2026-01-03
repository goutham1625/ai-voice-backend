import sqlite3

conn = sqlite3.connect("notes.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transcription TEXT,
    summary TEXT,
    actions TEXT
)
""")
conn.commit()

def save_note(transcription, summary, actions):
    cursor.execute(
        "INSERT INTO notes (transcription, summary, actions) VALUES (?, ?, ?)",
        (transcription, summary, str(actions))
    )
    conn.commit()

def get_notes():
    cursor.execute("SELECT * FROM notes ORDER BY id DESC")
    return cursor.fetchall()
