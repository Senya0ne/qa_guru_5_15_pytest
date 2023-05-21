"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser

from model.page import GithubPage


@pytest.fixture(params=[("1280x960"), ("1280x800"), ("360x640"), ("400x628")])
def browsers(request):
    size = request.param.split('x')
    browser.config.window_width = size[0]
    browser.config.window_height = size[1]

    yield browser

    browser.quit()


def is_desktop():
    width, height = browser.driver.get_window_size().values()
    return int(width) / int(height) > 1.25


parametrize_browsers = pytest.mark.parametrize("browsers", [("1280x960"), ("1280x800"), ("360x640"), ("400x628")],
                                               indirect=True)


@parametrize_browsers
@pytest.mark.skipif(is_desktop, reason="Пропустить, если разрешение мобильное")
def test_github_desktop(browsers):
    page = GithubPage()
    page.open_main_page()
    page.go_to_sign_in()
    page.have_texts_sign_in_form()


@parametrize_browsers
@pytest.mark.skipif(not is_desktop, reason="Пропустить, если разрешение декстопное")
def test_github_mobile(browsers):
    page = GithubPage()
    page.open_main_page()
    page.go_to_burger()
    page.go_to_sign_in()
    page.have_texts_sign_in_form()
