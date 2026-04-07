from selenium.webdriver.common.by import By


class BaseLocators:

    email_input = [By.XPATH, "//input[@name='email']"]

    password_input = [By.XPATH, "//input[@name='password']"]
