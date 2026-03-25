import json
from pathlib import Path

def load_credentials():
    data_path = Path(__file__).parent.parent / "test_data" / "user_credentials.json"
    with open(data_path) as file:
        return json.load(file)