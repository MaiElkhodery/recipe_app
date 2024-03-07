from django.shortcuts import render, get_object_or_404
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request=request,template_name='recipes.html',context={'recipes' : recipes})

def recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request=request,template_name='recipe_details.html',context={'recipe' : recipe})
