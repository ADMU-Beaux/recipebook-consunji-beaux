from django.shortcuts import render
from .models import Recipe, Ingredient

# Recipe list view
def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }
    return render(request, 'recipe_list.html', ctx)

def recipe_detail(request, id):
    recipe_name = Recipe.object.get(id=id).name
    ingredients = Ingredient.objects.filter(recipe__recipe__name=str(recipe_name))
    ctx = {
        "name": recipe_name,
        "ingredients": ingredients
    }    
    return render(request, 'recipe.html', ctx)