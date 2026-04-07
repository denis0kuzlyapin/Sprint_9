from pages.base_page import BasePage
from locators.header_locators import HeaderForUnauthorizedUser


class HeaderUnauth(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderForUnauthorizedUser()

    def click_create_account_in_header(self):
        self.click(self.locators.create_account_in_header)
        return self

    def wait_clickable_create_account(self):
        self.wait_clickable(self.locators.create_account_in_header)
        return self

    def click_recipe_header(self):
        self.click(self.locators.recipe_header_btn)
        return self

    def click_enter_in_header(self):
        self.click(self.locators.enter_in_header_btn)
