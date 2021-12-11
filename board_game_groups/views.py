from django.shortcuts import render
from .models import Game

def index(request):
    return render(request, 'board_game_groups/index.html')

def games(request):
    games = Game.objects.order_by('date_added')
    context = {'games' : games}
    return render(request, 'board_game_groups/games.html', context)