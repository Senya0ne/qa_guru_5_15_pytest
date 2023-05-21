"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene.support.shared import browser

from model.page import GithubPage


@pytest.fixture
def pc_browser():
    browser.config.window_width = '1280'
    browser.config.window_height = '960'

    yield

    browser.quit()


@pytest.fixture
def mobile_browser():
    browser.config.window_width = '400'
    browser.config.window_height = '628'

    yield

    browser.quit()


def test_github_desktop(pc_browser):
    page = GithubPage()
    page.open_main_page()
    page.go_to_sign_in()
    page.have_texts_sign_in_form()


def test_github_mobile(mobile_browser):
    page = GithubPage()
    page.open_main_page()
    page.go_to_burger()
    page.go_to_sign_in()
    page.have_texts_sign_in_form()
