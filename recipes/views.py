
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe


def home(request):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
        ).order_by('-id')
    )
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):    
    # recipes = Recipe.objects.filter(
    #    category__id = category_id,
    #    is_published = True,
    # ).order_by('-id')

    # if not recipes:
    #    raise Http404('Not found 😢😢😢😢')
    # else: 
    #    return render(request, 'recipes/pages/category.html', context={
    #        'recipes': recipes,
    #        'title': f'{recipes.first().category.name}'
    # })

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    # recipe =  Recipe.objects.filter(ss
    #        pk = id,
    #        is_published = True
    #    ).order_by('-id').first()
    recipe = get_object_or_404(Recipe, id=id, is_published=True,)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_datail_page': True,
    })
