from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms.recipe_form import RecipeForm,IngredientForm, IngredientFormSet
from django.urls import reverse
from django.http import JsonResponse

def home(request):
    recipes = Recipe.objects.all()
    return render(request=request,template_name='recipes.html',context={'recipes' : recipes})

def recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request=request,template_name='recipe_details.html',context={'recipe' : recipe})

def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid() :
            recipe_form.save()
            if request.is_ajax():
                return JsonResponse({'success': True})
            else:
                return redirect('add_ingredients')
    else:
        recipe_form = RecipeForm()
    return render(request=request,template_name='recipe_form.html',context={'recipe_form': recipe_form})

def add_recipe_ingredients(request):
    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid() :
            ingredient_form.save()
            return redirect('add_ingredients')
    else:
        ingredient_form = RecipeForm()
    return render(request=request,template_name='ingredient_form.html',context={'ingredient_form': ingredient_form})
        