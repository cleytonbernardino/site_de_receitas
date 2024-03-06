from django.urls import path

from .views import AuthorCreateView, AuthorsView, RecipeView

app_name = 'recipe'

urlpatterns = [
    path('recipe/', RecipeView.as_view(), name='create_and_get_all_recipes'),
    path('recipe/<int:id>/',
         RecipeView.as_view(), name='detail_update_delete_recipes'
         ),
    path('author/', AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:id>/',
         AuthorsView.as_view(), name='get_update_delete_author'
         )
]
