from django import forms
from recipe.models import Recipe, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'category', 'time_cooked','picture']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}), 
        }
        
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'unit', 'quantity', 'optional','recipe']
        
IngredientFormSet = forms.inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1, can_delete=True)