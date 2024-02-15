from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/1', recipe_1, name='recipe-1'),
    path('recipe/2', recipe_2, name='recipe-1'),
]

app_name = "ledger"