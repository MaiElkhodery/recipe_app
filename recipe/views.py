from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms.recipe_form import RecipeForm,IngredientForm, IngredientFormSet
from django.urls import reverse

def home(request):
    recipes = Recipe.objects.all()
    return render(request=request,template_name='recipes.html',context={'recipes' : recipes})

def recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request=request,template_name='recipe_details.html',context={'recipe' : recipe})

def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_form_set = IngredientFormSet(request.POST)
        if recipe_form.is_valid() and ingredient_form_set.is_valid():
            recipe = recipe_form.save()
            for form in ingredient_form_set:
                ingredient = form.save(commit = False)
                ingredient.recipe = recipe
                ingredient.save()
            return redirect(reverse('home'))
            
    else:
        recipe_form = RecipeForm()
        ingredient_formset = IngredientFormSet()
    return render(request=request,template_name='recipe_form.html',context={'recipe_form': recipe_form, 'ingredient_formset': ingredient_formset})
        