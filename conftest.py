import time

import pytest
from playwright.async_api import Playwright

from utils.data_reader import load_credentials

@pytest.fixture(scope="session")
def credentials():
    return load_credentials()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Select browser"
    )



@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(
            headless=False,
            channel="chrome"
        )
        print("Chrome launched")

    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
        print("Firefox launched")

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()

