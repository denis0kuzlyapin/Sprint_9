import allure
from data import RecipeData
from pages.create_recipe_page import CreateRecipePage
from pages.header_auth import HeaderAuth
from pages.auth_page import AuthPage


class TestCreatingRecipe:

    @allure.title("Создание рецепта авторизованным пользователем")
    @allure.description("Тест проверяет создание нового рецепта с ингредиентами")
    def test_create_recipe(self, driver, logout_after_test):

        auth_page = AuthPage(driver)
        recipe_page = CreateRecipePage(driver)
        header_page = HeaderAuth(driver)

        with allure.step("Открыть страницу авторизации"):
            auth_page.open_auth_page()

        with allure.step("Авторизоваться"):
            auth_page.login_with_static_data()

        with allure.step("Дождаться кликабельности кнопки 'Создать рецепт'"):
            header_page.wait_clickable_create_recipe()

        with allure.step("Нажать 'Создать рецепт'"):
            header_page.click_create_recipe()

        with allure.step("Дождаться кликабельности поля 'Название рецепта'"):
            recipe_page.wait_clickable_name_recipe()

        with allure.step("Ввести название рецепта"):
            recipe_name = RecipeData.get_recipe_name()
            recipe_page.fill_recipe_name(recipe_name)

        with allure.step("Указать время приготовления"):
            cooking_time = RecipeData.get_cooking_time()
            recipe_page.fill_cooking_time(cooking_time)

        with allure.step("Заполнить поле 'Описание рецепта'"):
            description = RecipeData.get_description()
            recipe_page.fill_description(description)

        with allure.step("Добавить фотографию рецепта"):
            recipe_page.upload_image("recipe.jpg")

        # Добавляем ингредиенты из списка
        ingredients = RecipeData.get_ingredients()

        with allure.step(f"Добавить ингредиент '{ingredients[0]['name']}' {ingredients[0]['grams']}г"):
            recipe_page.fill_ingredients(ingredients[0]["name"])
            recipe_page.fill_grams(str(ingredients[0]["grams"]))
            recipe_page.click_add_ingredient()

        with allure.step(f"Добавить ингредиент '{ingredients[1]['name']}' {ingredients[1]['grams']}г"):
            recipe_page.fill_ingredients(ingredients[1]["name"])
            recipe_page.fill_grams(str(ingredients[1]["grams"]))
            recipe_page.click_add_ingredient()

        with allure.step("Нажать 'Создать рецепт'"):
            recipe_page.click_create_recipe_button()

        with allure.step("Дождаться появления карточки созданного рецепта"):
            recipe_page.wait_visible_recipe_card()

        with allure.step("Сохранить название созданного рецепта"):
            name_from_card = recipe_page.get_recipe_name_from_card()

        with allure.step("Проверить, что карточка созданного рецепта отображается"):
            assert recipe_page.is_recipe_card_displayed()

        with allure.step(
            "Проверить, что название рецепта совпадает с указанным при создании"
        ):
            assert name_from_card == recipe_name
