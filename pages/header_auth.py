from pages.base_page import BasePage
from locators.header_locators import HeaderForAuthorizedUser


class HeaderAuth(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = HeaderForAuthorizedUser()

    def logout(self):
        self.click(self.locators.logout_btn)

    def is_logout_btn_visible(self):
        return self.is_element_visible(self.locators.logout_btn)

    def wait_visible_logout_btn(self):
        self.wait_visible(self.locators.logout_btn)

    def wait_clickable_create_recipe(self):
        self.wait_clickable(self.locators.create_recipe)

    def click_create_recipe(self):
        self.click(self.locators.create_recipe)
