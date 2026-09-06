import os


NOTES_FOLDER = "notes"


def save_notes(topic, notes):
    os.makedirs(NOTES_FOLDER, exist_ok=True)

    filename = topic.lower().replace(" ", "_") + ".txt"
    filepath = os.path.join(NOTES_FOLDER, filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write("AI STUDY ASSISTANT\n")
        file.write("==================\n\n")
        file.write(f"Topic: {topic.title()}\n\n")
        file.write(notes)

    return filepath