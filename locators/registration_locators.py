from selenium.webdriver.common.by import By


class RegistrationLocators:

    first_name_input = [By.XPATH, "//input[@name='first_name']"]

    last_name_input = [By.XPATH, "//input[@name='last_name']"]

    username_input = [By.XPATH, "//input[@name='username']"]

    create_btn = [By.XPATH, "//button[contains(text(),'Создать аккаунт')]"]
