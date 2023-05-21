"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene.support.shared import browser

from model.page import GithubPage


@pytest.fixture(params=["pc_browser", "mobile_browser"])
def browsers(request):
    if request.param == "pc_browser":
        browser.config.window_width = '1280'
        browser.config.window_height = '960'
    if request.param == "mobile_browser":
        browser.config.window_width = '400'
        browser.config.window_height = '628'
    yield browser
    browser.quit()


pc_browser = pytest.mark.parametrize("browsers", ["pc_browser"], indirect=True)
mobile_browser = pytest.mark.parametrize("browsers", ["mobile_browser"], indirect=True)


@pc_browser
def test_github_desktop(browsers):
    page = GithubPage()
    page.open_main_page()
    page.go_to_sign_in()
    page.have_texts_sign_in_form()


@mobile_browser
def test_github_mobile(browsers):
    page = GithubPage()
    page.open_main_page()
    page.go_to_burger()
    page.go_to_sign_in()
    page.have_texts_sign_in_form()
