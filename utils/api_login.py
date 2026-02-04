import os
import requests
from dotenv import load_dotenv

load_dotenv()

LOGIN_URL = "https://backend.pikaresume.com/auth/email-signin"

def api_login():
    payload = {
        "email": os.getenv("PIKA_EMAIL"),
        "password": os.getenv("PIKA_PASSWORD")
    }

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://pikaresume.com",
        "Referer": "https://pikaresume.com",
        "User-Agent": "Mozilla/5.0"
    }

    session = requests.Session()
    response = session.post(LOGIN_URL, json=payload, headers=headers)

    # Backend returns 201 on success
    assert response.status_code in (200, 201), (
        f"API Login Failed: {response.status_code} {response.text}"
    )

    return session.cookies
