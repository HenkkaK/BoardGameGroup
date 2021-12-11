from django.urls import path
from . import views
app_name = 'board_game_groups'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all games
    path('games/', views.games, name='games'),
]