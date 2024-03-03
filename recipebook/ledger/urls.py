from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list', recipe_list, name='recipe-list'),
    path('recipe/<int:id>', recipe_detail, name='recipe-detail')
]

app_name = "ledger"