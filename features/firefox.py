from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


class Browser():
    def __init__(self):
        self.browser = self.createBrowser()
        self.browser.implicitly_wait(60)

    def createBrowser(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--window-size=1920x1080")
        firefox_options.add_argument("--disable-application-cache")
        firefox_options.add_argument("--verbose")
        firefox_options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(options=firefox_options)
        return driver

    def clearCache(self):
        self.browser.delete_all_cookies()

    def wait(self, seconds=5):
        time.sleep(seconds)



@fixture
def browser_firefox(context, **kwargs):
    context.browser = Browser()
    yield context.browser
    context.browser.browser.quit()


def before_all(context):
    use_fixture(browser_firefox, context)
