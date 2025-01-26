from django.contrib import admin
from .models import Category, Recipe


"""
    Para registar  a model na Admin
"""

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
    
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...