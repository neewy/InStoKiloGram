from django.contrib import admin

# Register your models here.
from Recipes.models import Recipe

admin.site.register(Recipe)