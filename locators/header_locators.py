from selenium.webdriver.common.by import By


class HeaderForUnauthorizedUser:

    create_account_in_header = [By.XPATH, "//a[contains(text(), 'Создать аккаунт')]"]

    enter_in_header_btn = [By.XPATH, "//header//a[contains(text(), 'Войти')]"]

    recipe_header_btn = [By.XPATH, "//header//a[contains(text(), 'Рецепты')]"]


class HeaderForAuthorizedUser:

    create_recipe = [By.XPATH, "//a[contains(text(), 'Создать рецепт')]"]

    logout_btn = [By.XPATH, "//a[contains(text(), 'Выход')]"]
