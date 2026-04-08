from constants import Url
from data import TestUser
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.auth_locators import AuthLocators


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AuthLocators()
        self.base_locators = BaseLocators()

    def open_auth_page(self):
        self.open_page(Url.AUTH_URL)

    def is_enter_visible(self):
        return self.is_element_visible(self.locators.enter_btn)

    def click_enter_button(self):
        self.click(self.locators.enter_btn)

    def login_with_static_data(self):
        self.send_keys(self.base_locators.email_input, TestUser.USERNAME)
        self.send_keys(self.base_locators.password_input, TestUser.PASSWORD)

        self.click(self.locators.enter_btn)
        self.wait_url_to_be(Url.RECIPES_URL)
