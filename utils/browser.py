from os import environ
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = environ.get('CHROMEDRIVER_NAME', 'chromedriver')
CHROMEDRIVER_PATH = str(ROOT_PATH / 'bin' / CHROMEDRIVER_NAME)


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    if environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')

    chrome_services = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_services, options=chrome_options)
    return browser
