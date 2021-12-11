from django.shortcuts import render
from .models import Game

def index(request):
    return render(request, 'board_game_groups/index.html')

def games(request):
    games = Game.objects.order_by('date_added')
    context = {'games' : games}
    return render(request, 'board_game_groups/games.html', context)

def game(request, game_id):
    game = Game.objects.get(id=game_id)
    borrows = game.borrow_set.order_by('-date_added')
    context = {'game' : game, 'borrows': borrows}
    return render(request, 'board_game_groups/game.html', context)