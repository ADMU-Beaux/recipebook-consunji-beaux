from django.db import models
from djange.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.name)])
    

class Recipe(models.Model):
    name = models.CharField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('recipe-detail', args=[str(self.name)])
    
class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')