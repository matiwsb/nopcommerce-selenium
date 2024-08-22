import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="specify the browser: chrome, firefox, edge")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    return driver

    # driver = webdriver.Chrome
    # return driver

