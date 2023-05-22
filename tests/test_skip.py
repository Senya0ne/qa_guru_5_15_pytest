"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selene.support.shared import browser

from model.page import GithubPage


@pytest.fixture(params=[("1280", "960"), ("1280", "800"), ("360", "640"), ("400", "628")])
def browsers(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    desktop = int(width) / int(height) > 1.25

    yield browser, desktop

    browser.quit()


def test_github_desktop(browsers):
    if browsers[1] is True:
        page = GithubPage()
        page.open_main_page()
        page.go_to_sign_in()
        page.have_texts_sign_in_form()
    else:
        pytest.skip(reason='Тест будет пропущен, так как разрешение экрана мобильное')


def test_github_mobile(browsers):
    if browsers[1] is False:
        page = GithubPage()
        page.open_main_page()
        page.go_to_burger()
        page.go_to_sign_in()
        page.have_texts_sign_in_form()
    else:
        pytest.skip(reason='Тест будет пропущен, так как разрешение экрана десктопное')
