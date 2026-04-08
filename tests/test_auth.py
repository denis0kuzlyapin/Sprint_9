import allure

from constants import Url
from pages.base_page import BasePage
from pages.auth_page import AuthPage
from pages.header_auth import HeaderAuth


class TestAuthUser:

    @allure.title("Авторизация пользователя")
    def test_auth_user(self, driver, logout_after_test):

        header_auth_page = HeaderAuth(driver)
        auth_page = AuthPage(driver)

        with allure.step("Открыть страницу авторизации"):
            auth_page.open_auth_page()

        with allure.step("Авторизоваться"):
            auth_page.login_with_static_data()

        with allure.step("Дождаться появления кнопки 'Выйти'"):
            header_auth_page.wait_visible_logout_btn()

        with allure.step("Сохранить текущий url"):
            current_url_auth = auth_page.get_current_url()

        with allure.step("Убедиться, что произошёл переход на главную страницу"):
            assert current_url_auth == Url.RECIPES_URL

        with allure.step("Убедиться, что появилась кнопка 'Выйти'"):
            assert header_auth_page.is_logout_btn_visible() == True
