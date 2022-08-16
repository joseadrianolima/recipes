from django.test import TestCase
from django.urls import reverse


class RecipeURLsTest(TestCase):
    def teste_recipe_home_urls_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def teste_recipe_category_urls_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def teste_recipe_recipe_urls_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')
