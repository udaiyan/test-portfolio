import pytest
import requests
from playwright.sync_api import Page, expect
import time
import subprocess
import os
import signal


# Server management
@pytest.fixture(scope="session")
def server():
    """Start the FastAPI server for testing"""
    # Change to the project root directory
    original_dir = os.getcwd()
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)

    # Start the server
    process = subprocess.Popen(
        ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for server to start
    time.sleep(3)

    # Verify server is running
    max_retries = 5
    for i in range(max_retries):
        try:
            response = requests.get("http://localhost:8000/api/health")
            if response.status_code == 200:
                break
        except requests.exceptions.ConnectionError:
            if i == max_retries - 1:
                process.kill()
                raise Exception("Server failed to start")
            time.sleep(2)

    yield process

    # Cleanup: stop the server
    process.terminate()
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()

    os.chdir(original_dir)


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the application"""
    return "http://localhost:8000"


@pytest.fixture
def api_client(server, base_url):
    """HTTP client for API testing"""
    class APIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()

        def get(self, endpoint, **kwargs):
            return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

        def post(self, endpoint, **kwargs):
            return self.session.post(f"{self.base_url}{endpoint}", **kwargs)

        def delete(self, endpoint, **kwargs):
            return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)

        def close(self):
            self.session.close()

    client = APIClient(base_url)
    yield client
    client.close()


@pytest.fixture
def page(server, page: Page):
    """Playwright page fixture with server dependency"""
    # The page fixture is provided by pytest-playwright
    # We just add the server dependency here
    yield page


# Browser configuration (optional customization)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Customize browser context for all tests"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1280,
            "height": 720,
        },
        "ignore_https_errors": True,
    }


# Utility fixtures
@pytest.fixture
def wait_for_element():
    """Helper fixture for waiting for elements"""
    def _wait(page: Page, selector: str, timeout: int = 5000):
        page.wait_for_selector(selector, timeout=timeout)
    return _wait
