import webbrowser
import pytest

@pytest.fixture()
def setup():
    driver = webbrowser.Chrome
    return driver
