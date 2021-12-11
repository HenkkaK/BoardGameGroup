from django.urls import path
from . import views
app_name = 'board_game_groups'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all games
    path('games/', views.games, name='games'),
    # Detail page for a game
    path('games/<int:game_id>/', views.game, name='game'),
    # Page for adding a game
    path('new_game/', views.new_game, name='new_game'),
    # Page for a new borrow
    path('new_borrow/<int:game_id>', views.new_borrow, name='new_borrow'),
]