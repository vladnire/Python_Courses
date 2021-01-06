import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser")

    return driver


def pytest_addoption(parser):
    """Get value from CLI"""
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    """Will return the Browser value to setup method"""
    return request.config.getoption("--browser")


def pytest_configure(config):
    """Hook for Adding Environment info to HTML report"""
    config._metadata['Prokect Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Vlad'


@pytest.mark.optionalhool
def pytest_metadata(metadata):
    """Hook to delete/modify environment info to HTML report"""
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
