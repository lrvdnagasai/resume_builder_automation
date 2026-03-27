import allure
import pytest
from utils.data_reader import load_credentials
from utils.api_login import api_login


@pytest.fixture(scope="session")
def credentials():
    return load_credentials()


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=headless, channel="chrome")
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    yield page

    trace_path = f"allure-results/{request.node.name}_trace.zip"
    context.tracing.stop(path=trace_path)
    allure.attach.file(
        trace_path,
        name="Playwright Trace",
        attachment_type=allure.attachment_type.ZIP
    )

    context.close()
    browser.close()


@pytest.fixture
def authenticated_page(playwright, request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=headless, channel="chrome")
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=headless)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    cookies = api_login()
    context.add_cookies([
        {
            "name": c.name,
            "value": c.value,
            "domain": ".pikaresume.com",
            "path": "/"
        }
        for c in cookies
    ])

    page = context.new_page()
    page.goto("https://pikaresume.com/dashboard")

    yield page

    trace_path = f"allure-results/{request.node.name}_trace.zip"
    context.tracing.stop(path=trace_path)
    allure.attach.file(
        trace_path,
        name="Playwright Trace",
        attachment_type=allure.attachment_type.ZIP
    )

    context.close()
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("authenticated_page") or item.funcargs.get("browserInstance")
        if page:
            allure.attach(
                page.screenshot(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )