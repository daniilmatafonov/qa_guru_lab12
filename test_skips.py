import pytest
from selene import have
from selene.support.shared import browser

url = 'https://github.com/'
browserName = 'chrome'
signInExpectedText = "Sign in to GitHub"


@pytest.fixture(scope='function')
def browser_config():
    browser.config.browser_name = browserName
    browser.config.window_width = 320
    browser.config._window_height = 480


def test_github_check_mobile():
    if browser._config.window_width > 1100:
        pytest.skip('Desktop test')
    browser.element('button[aria-label="Toggle navigation"').click()
    browser.element('a[href="/login"]').click()
    browser.element('.auth-form-header').should(have.text(signInExpectedText))


def test_github_check_desktop():
    if browser._config.window_width < 1100:
        pytest.skip('Mobile test')
    browser.element("a.flex-shrink-0:nth-child(1)").click()
    browser.element('.auth-form-header').should(have.text(signInExpectedText))