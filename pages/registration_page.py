from constants import Url
from helpers import GenDataForUser
from pages.base_page import BasePage
from locators.base_locators import BaseLocators
from locators.registration_locators import RegistrationLocators


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.reg_locators = RegistrationLocators()
        self.base_locators = BaseLocators()

    def get_registration_page(self):
        self.open_page(Url.AUTH_URL)

    def wait_clickable_username_input(self):
        self.wait_clickable(self.reg_locators.username_input)

    def enter_registration_form(self):
        first_name = GenDataForUser.gen_first_name()
        last_name = GenDataForUser.gen_last_name()
        username = GenDataForUser.gen_username()
        email = GenDataForUser.gen_email()
        password = GenDataForUser.gen_password()
        self.send_keys(self.reg_locators.first_name_input, first_name)
        self.send_keys(self.reg_locators.last_name_input, last_name)
        self.send_keys(self.reg_locators.username_input, username)
        self.send_keys(self.base_locators.email_input, email)
        self.send_keys(self.base_locators.password_input, password)
        return {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "password": password,
        }

    def click_create_account(self):
        self.click(self.reg_locators.create_btn)

    def wait_url_to_be_auth(self):
        self.wait_url_to_be(Url.AUTH_URL)
