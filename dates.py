def detect_due_dates(actions):
    dated_actions = []

    for action in actions:
        due = "No date"

        if "today" in action:
            due = "Today"
        elif "tomorrow" in action:
            due = "Tomorrow"
        elif "next week" in action:
            due = "Next Week"
        elif "monday" in action:
            due = "Monday"

        dated_actions.append({
            "task": action,
            "due": due
        })

    return dated_actions
