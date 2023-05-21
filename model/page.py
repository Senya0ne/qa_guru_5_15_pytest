from selene.support.conditions import be, have
from selene.support.shared import browser


class GithubPage:
    def open_main_page(self):
        browser.open('https:/github.com')

    def go_to_burger(self):
        browser.element(".Button--link").click()

    def go_to_sign_in(self):
        browser.element("a[href='/login']").click()

    def have_texts_sign_in_form(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
        browser.element("[for='login_field']").should(have.text('Username or email address'))
        browser.element("[for='password']").should(have.text('Password'))
