from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# User models
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.CharField(max_length=255)

# Recipe models
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])
    

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe', args=[str(self.pk)])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

