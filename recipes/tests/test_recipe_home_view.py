
from importlib.resources import path
from unittest.mock import patch

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here', 
            response.content.decode('utf-8')
        )

    def test_recipe_home_templates_loads_recipies(self):
        self.make_recipe(title='Title')
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_templates_loads_not_published_recipies(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here', 
            response.content.decode('utf-8')
        )

    @patch('recipes.views.PER_PAGE', new=3)
    def test_recipe_home_templates_loads_correct_per_page_environ(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_date': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']
        paginator = recipes.paginator
        self.assertEqual(paginator.num_pages, 3)
        self.assertEqual(len(paginator.get_page(1)), 3)
        self.assertEqual(len(paginator.get_page(3)), 2)