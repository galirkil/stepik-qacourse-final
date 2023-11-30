import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language'
                     )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    if browser_name == 'chrome':
        print('\nstart browser for test..')
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': language}
        )
        driver = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('\nstart browser for test..')
        options = FoxOptions()
        options.set_preference('intl.accept_languages', language)
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield driver
    print('\nquit browser..')
    driver.quit()
