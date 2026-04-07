from selenium.webdriver.common.by import By


class CreateRecipeLocators:

    recipe_name_input = [
        By.XPATH,
        "//*[contains(text(), 'Название рецепта')]/ancestor::label//input",
    ]

    ingredients_input = [
        By.XPATH,
        "//*[contains(text(), 'Ингредиенты')]/ancestor::label//input",
    ]

    first_ingredient_in_dd = [By.CSS_SELECTOR, "div.styles_container__3ukwm > div:first-child"]

    add_ingredients = [By.XPATH, "//div[contains(text(),'Добавить ингредиент')]"]

    grams_input = [By.CSS_SELECTOR, "input.styles_ingredientsAmountValue__2matT"]

    cooking_time = [
        By.XPATH,
        "//*[contains(text(), 'Время приготовления')]/ancestor::label//input",
    ]

    description_recipe = [
        By.XPATH,
        "//*[contains(text(), 'Описание рецепта')]/ancestor::label//textarea",
    ]

    select_file = [By.CSS_SELECTOR, "input[type='file']"]

    create_recipe_btn = [By.XPATH, "//button[contains(text(), 'Создать рецепт')]"]

    recipe_card = [By.CSS_SELECTOR, "div.styles_single-card__info__2_cny"]

    name_recipe = [
        By.XPATH,
        "//h1",
    ]
