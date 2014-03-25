from lettuce.django import django_url
from nose.tools import assert_equals, assert_true


class BasePage(object):
    url = None

    def __init__(self, browser):
        self.browser = browser

    def visit(self):
        self.browser.visit(django_url(self.url))

    def validate_url(self):
        assert self.browser.url == django_url(self.url)

    def fill(self, name, value):
        self.browser.fill(name, value)

    def submit(self):
        self.browser.find_by_css("form button").first.click()

    def click_link_by_text(self, text):
        self.browser.click_link_by_text(text)

    def click_by_css(self, css_selector):
        self.browser.find_by_css(css_selector).first.click()

    def click_link_by_partial_href(self, modal_id):
        self.browser.click_link_by_partial_href(modal_id)

    def click_link_by_href(self, modal_id):
        self.browser.click_link_by_href(modal_id)

    def click_by_name(self, name):
        self.browser.find_by_name(name).first.click()

    def _is_text_present(self, text, status=True):
        assert_equals(status, self.browser.is_text_present(text))

    def is_text_present(self, *texts, **kwargs):
        status = kwargs['status'] if 'status' in kwargs else True
        for text in texts:
            self._is_text_present(text, status)

    def fill_form(self, data):
        self.browser.fill_form(data)

    def click_by_id(self, id):
        self.browser.find_by_id(id).first.click()

    def check(self, value):
        self.browser.find_by_value(value).first.check()

    def select(self, name, value):
        self.browser.select(name, value)

    def is_element_present_by_value(self, value):
        assert_true(self.browser.is_element_present_by_value(value))

    def find_by_id(self, id, status=True):
        assert_equals(status, self.is_element_present_by_id(id))
