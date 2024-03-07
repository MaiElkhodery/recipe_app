from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('recipe/<int:recipe_id>', views.recipe, name = 'recipe_detail')
]

