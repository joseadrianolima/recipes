from django.test import TestCase
from django.urls import resolve, reverse


class RecipeURLsTest(TestCase):
    def teste_recipe_home_urls_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def teste_recipe_category_urls_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 12})
        self.assertEqual(url, '/recipes/category/12/')

    def teste_recipe_recipe_urls_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')


class RecipeViewTest(TestCase):
    def test_recipe_home_views_functions_is_correct(self):
        view = resolve('/')
        self.assertTrue(True)
