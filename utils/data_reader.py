import json
from pathlib import Path

def load_credentials():
    data_path = "/Users/nagasailakkoju/PycharmProjects/resume_builder_automation/test_data/user_credentials.json"
    with open(data_path) as file:
        return json.load(file)