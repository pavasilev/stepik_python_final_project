mport pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--languages', action='store', default="ru",
                     help="Choose language: ru or en")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("languages")
    browser_name = request.config.getoption("browser_name")
    browser = None
    options_chrome = Options()
    options_firefox = FirefoxOptions()
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options_firefox.set_preference("intl.accept_languages", user_language)
    if browser_name == "chrome":
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        options = Options()
        options_firefox.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()