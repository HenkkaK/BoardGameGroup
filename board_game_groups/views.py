from django.shortcuts import render, redirect
from .models import Game
from .forms import GameForm, BorrowForm

def index(request):
    return render(request, 'board_game_groups/index.html')

def games(request):
    games = Game.objects.order_by('date_added')
    context = {'games' : games}
    return render(request, 'board_game_groups/games.html', context)

def game(request, game_id):
    game = Game.objects.get(id=game_id)
    borrows = game.borrow_set.order_by('-Borrow_date')
    context = {'game' : game, 'borrows': borrows}
    return render(request, 'board_game_groups/game.html', context)

def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_groups:games')
    context = {'form' : form}
    return render(request, 'board_game_groups/new_game.html', context)

def new_borrow(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        form = BorrowForm()
    else:
        form = BorrowForm(data=request.POST)
        if form.is_valid():
            new_borrow = form.save(commit=False)
            new_borrow.game = game
            new_borrow.save()
            return redirect('board_game_group:game', game_id=game_id)

    context = {'game' : game, 'form' : form}
    return render(request, 'board_game_groups/new_borrow.html', context)