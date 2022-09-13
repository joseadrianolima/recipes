from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import Recipe, RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False

        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False',
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False',
        )


    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length+10))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_string_representation(self):
        strNameRecipeCategory = "CategoryRecipe"
        #category = self.make_category(strNameRecipeCategory)
        self.recipe.title = strNameRecipeCategory
        self.recipe.save()
        self.assertEqual(str(self.recipe), strNameRecipeCategory)
        self.recipe.full_clean()

    def test_recipe_category_name_max_length(self):
        self.recipe.title = 'A' * (65)
        self.assertRaises(ValidationError)
        self.recipe.full_clean()
