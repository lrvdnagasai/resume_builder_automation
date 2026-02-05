import os
import requests

LOGIN_URL = "https://backend.pikaresume.com/auth/email-signin"

def api_login():
    email = os.environ.get("PIKA_EMAIL")
    password = os.environ.get("PIKA_PASSWORD")

    if not email or not password:
        raise RuntimeError(
            "Environment variables PIKA_EMAIL and PIKA_PASSWORD must be set.\n"
            "For local run use:\n"
            "export PIKA_EMAIL='your_email'\n"
            "export PIKA_PASSWORD='your_password'"
        )

    payload = {
        "email": email,
        "password": password
    }

    headers = {
        "Content-Type": "application/json",
        "Origin": "https://pikaresume.com",
        "Referer": "https://pikaresume.com",
        "User-Agent": "Mozilla/5.0"
    }

    session = requests.Session()
    response = session.post(LOGIN_URL, json=payload, headers=headers)

    assert response.status_code in (200, 201), (
        f"Login failed: {response.status_code} {response.text}"
    )

    return session.cookies
