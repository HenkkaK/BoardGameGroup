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
    path('new_borrow/<int:game_id>/', views.new_borrow, name='new_borrow'),
    # Page for editing a borrow
    path('edit_borrow/<int:borrow_id>/', views.edit_borrow, name='edit_borrow'),
    # Page for editing a game
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
]