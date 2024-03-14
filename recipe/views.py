from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms.recipe_form import RecipeForm,IngredientForm
from django.urls import reverse

def home(request):
    recipes = Recipe.objects.all()
    return render(request=request,template_name='recipes.html',context={'recipes' : recipes})

def recipe(request,recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = recipe.ingredient_set.all() 
    return render(request, 'recipe_details.html', {'recipe': recipe, 'ingredients': ingredients})
    # recipe = get_object_or_404(Recipe, pk=recipe_id)
    # return render(request=request,template_name='recipe_details.html',context={'recipe' : recipe})

def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST,request.FILES)
        
        if recipe_form.is_valid() :
            new_recipe = recipe_form.save()
            return redirect('add_ingredients',recipe_id= new_recipe.id)
    else:
        recipe_form = RecipeForm()
    return render(request=request,template_name='recipe_form.html',context={'recipe_form': recipe_form})

def add_recipe_ingredients(request, recipe_id):
    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid() :
            ingredient = ingredient_form.save(commit=False)
            recipe = Recipe.objects.get(pk=recipe_id)
            ingredient.recipe = recipe
            ingredient.save()
            print('ingredients: ',ingredient_form.cleaned_data)
            return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        ingredient_form = IngredientForm()
    return render(request=request,template_name='ingredient_form.html',context={'ingredient_form': ingredient_form})
        