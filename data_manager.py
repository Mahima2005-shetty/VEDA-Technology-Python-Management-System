import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def load_data(filename):
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / filename

    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {filename}. Starting with empty data.")
        return []


def save_data(filename, data):
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / filename

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def next_id(records):
    if not records:
        return 1
    return max(int(item.get("id", 0)) for item in records) + 1
