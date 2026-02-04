import os
import requests

LOGIN_URL = "https://backend.pikaresume.com/auth/email-signin"

def api_login():
    email = os.getenv("PIKA_EMAIL")
    password = os.getenv("PIKA_PASSWORD")

    assert email, "PIKA_EMAIL not set"
    assert password, "PIKA_PASSWORD not set"

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
