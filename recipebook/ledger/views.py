from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, Ingredient


# Recipe list view
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "logged_in": request.user.is_authenticated,
        "recipes": recipes
    }
    return render(request, 'recipe_list.html', ctx)

# Recipe detail view
@login_required
def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    ctx = {
        "logged_in": request.user.is_authenticated,
        "recipe": recipe
    } 
    return render(request, 'recipe_detail.html', ctx)