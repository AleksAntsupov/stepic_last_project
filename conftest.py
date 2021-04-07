import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Выбор языка в консоли
def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = 'en',
                    help = "Choose your language, please!")
#Выбор языка в консоли
@pytest.fixture(scope="function")
def browser(request):
    language_page = request.config.getoption('--language')
    language = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_page})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()