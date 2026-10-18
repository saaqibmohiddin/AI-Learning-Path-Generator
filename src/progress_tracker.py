
import json
from pathlib import Path

PROGRESS_FILE = Path(__file__).resolve().parent.parent / "learning_progress.json"

def load_all_progress():
    if not PROGRESS_FILE.exists():
        return {}

    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}

def load_progress(profile_key):
    data = load_all_progress()
    completed = data.get(profile_key, [])
    return completed if isinstance(completed, list) else []

def save_progress(profile_key, completed_ids):
    data = load_all_progress()
    data[profile_key] = sorted(set(completed_ids))

    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(PROGRESS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def calculate_progress(total_topics, completed_topics):
    if total_topics <= 0:
        return 0

    percentage = (completed_topics / total_topics) * 100
    return round(min(100, percentage))