import pytest
from selene.support.by import link_text
from selene.support.shared import browser

url = 'https://github.com/'
browserName = 'chrome'

@pytest.fixture(scope='function')
def browser_config():
    browser.config.browser_name = browserName
    browser.config.window_width = 320
    browser.config._window_height = 480


def test_github_desktop(browser_config):
    if browser.config.window_width < 1000:
        pytest.skip('Window size for mobile version')
    browser.open(url)
    browser.element(link_text('Sign in')).click()


def test_github_mobile(browser_config):
    if browser.config.window_height > 1000:
        pytest.skip('Window size for browser version')
    browser.open(url)
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element(link_text('Sign in')).click()