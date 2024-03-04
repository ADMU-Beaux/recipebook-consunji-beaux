from django.shortcuts import render
from .models import Recipe, RecipeIngredient, Ingredient

# Recipe list view
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'recipe_list.html', ctx)

# Recipe detail view
def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    ctx = {
        "recipe": recipe
    } 
    return render(request, 'recipe_detail.html', ctx)