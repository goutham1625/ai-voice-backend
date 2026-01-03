import re

ACTION_VERBS = [
    "call", "email", "meet", "attend", "finish", "submit",
    "prepare", "review", "schedule", "plan", "complete"
]

def extract_action_items(text: str):
    sentences = re.split(r"[.\n]", text.lower())
    actions = []

    for s in sentences:
        for verb in ACTION_VERBS:
            if verb in s:
                actions.append(s.strip().capitalize())
                break

    return actions
