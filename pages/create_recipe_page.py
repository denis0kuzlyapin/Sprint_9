from pathlib import Path
from pages.base_page import BasePage
from locators.create_recipe_locators import CreateRecipeLocators


class CreateRecipePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CreateRecipeLocators()

    def fill_recipe_name(self, name):
        self.send_keys(self.locators.recipe_name_input, name)
        return self

    def fill_ingredients(self, ingredient_name):
        self.send_keys(self.locators.ingredients_input, ingredient_name)
        self.click_with_retry(self.locators.first_ingredient_in_dd)
        return self

    def click_add_ingredient(self):
        self.click(self.locators.add_ingredients)
        return self

    def fill_grams(self, grams):
        self.send_keys(self.locators.grams_input, grams)
        return self

    def fill_cooking_time(self, minutes):
        self.send_keys(self.locators.cooking_time, minutes)
        return self

    def fill_description(self, description):
        self.send_keys(self.locators.description_recipe, description)
        return self

    def upload_image(self, filename):
        app_dir = Path(__file__).parent.parent
        file_path = str(app_dir / "assets" / filename)
        self.send_keys_to_hidden_element(self.locators.select_file, file_path)
        return self

    def click_create_recipe_button(self):
        self.click(self.locators.create_recipe_btn)
        return self

    def is_recipe_card_displayed(self):
        return self.is_element_visible(self.locators.recipe_card)

    def get_recipe_name_from_card(self):
        return self.get_text(self.locators.name_recipe)

    def wait_visible_recipe_card(self):
        self.wait_visible(self.locators.recipe_card)
        return self

    def wait_clickable_name_recipe(self):
        self.wait_clickable(self.locators.name_recipe)
        return self

    def wait_clickable_create_recipe_btn(self):
        self.wait_clickable(self.locators.create_recipe_btn)
        return self
