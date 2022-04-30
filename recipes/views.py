from django.http import HttpResponse
from django.shortcuts import render

from main import make_recipe
from utils.recipes.factory import make_recipe
from . import models


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(15)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datail_page': True,
    })
