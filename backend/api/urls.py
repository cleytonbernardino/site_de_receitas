from django.urls import path

from .views import Recipe

app_name = 'recipe'

urlpatterns = [
    path('', Recipe.as_view(), name='recipe_view')
]
