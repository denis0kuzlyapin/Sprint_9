import allure

from constants import Url
from pages.header_unauth import HeaderUnauth
from pages.auth_page import AuthPage
from pages.registration_page import RegistrationPage


class TestRegistrationUser:

    @allure.title("Регистрация пользователя")
    @allure.description("Тест проверяет создание нового аккаунта']")
    def test_create_account(self, driver):

        reg_page = RegistrationPage(driver)

        with allure.step("Открыть страницу авторизации"):
            reg_page.get_registration_page()

        header_page = HeaderUnauth(driver)

        with allure.step("Дождаться кликабельности кнопки 'Создать аккаунт'"):
            header_page.wait_clickable_create_account()

        with allure.step("Нажать 'Создать аккаунт'"):
            header_page.click_create_account_in_header()

        with allure.step("Дождаться кликабельности поля 'Имя пользователя'"):
            reg_page.wait_clickable_username_input()

        with allure.step("Заполнить форму регистрации"):
            reg_page.enter_registration_form()

        with allure.step("Нажать 'Создать аккаунт' в нижней части формы"):
            reg_page.click_create_account()

        with allure.step("Дождаться редиректа на страницу авторизации"):
            reg_page.wait_url_to_be_auth()

        with allure.step("Сохранить текущий url"):
            current_url_auth = reg_page.get_current_url()

            auth_page = AuthPage(driver)

        with allure.step("Убедиться, что произошёл  переход на страницу авторизации"):

            assert current_url_auth == Url.AUTH_URL

        with allure.step("Убедиться, что отображается форма авторизации"):

            assert auth_page.is_enter_visible() == True
