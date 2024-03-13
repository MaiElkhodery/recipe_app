from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('recipe/<int:recipe_id>', views.recipe, name = 'recipe_detail'),
    path('add_recipe/',views.add_recipe,name='add recipe'),
    path('add_ingredients/',views.add_recipe_ingredients,name='add ingredients')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



