import pytest
from selene.support.by import link_text
from selene.support.shared import browser

url = 'https://github.com/'
browserName = 'chrome'


@pytest.fixture(scope='function')
def desktop_func():
    browser.config.browser_name = browserName
    browser.config.window_width = 1360
    browser.config._window_height = 768


@pytest.fixture(scope='function')
def mobile_func():
    browser.config.browser_name = browserName
    browser.config.window_width = 720
    browser.config._window_height = 1080


def test_github_signin_desktop(desktop_func):
    browser.open(url)
    browser.element(link_text('Sign in')).click()


def test_github_signin_mobile(mobile_func):
    browser.open(url)
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element(link_text('Sign in')).click()
