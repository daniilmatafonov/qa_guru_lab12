import pytest
from selene.support.by import link_text
from selene.support.shared import browser

url = 'https://github.com/'
params = pytest.fixture(params=[(320, 480), (1360, 768), (1600, 1200)])


@params
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_size):
    browser.config.window_width = browser_size.param[0]
    browser.config.window_height = browser_size.param[1]


@pytest.mark.parametrize("browser_size", [(1360, 768)], indirect=True)
def test_github_signin_desktop(browser_size):
    browser.open(url)
    browser.element(link_text('Sign in')).click()


@pytest.mark.parametrize("browser_size", [(320, 480)], indirect=True)
def test_github_signin_mobile(browser_size):
    browser.open(url)
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element(link_text('Sign in')).click()
