from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Recipe, RecipeIngredient, Ingredient, Profile

# User models
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Recipe models
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'updated_on', )
    inlines = [RecipeIngredientInline, ]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)