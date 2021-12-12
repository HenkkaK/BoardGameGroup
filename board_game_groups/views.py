from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Game, Borrow
from .forms import GameForm, BorrowForm

def index(request):
    return render(request, 'board_game_groups/index.html')

@login_required
def games(request):
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'board_game_groups/games.html', context)

@login_required
def game(request, game_id):
    game = Game.objects.get(id=game_id)
    borrows = game.borrow_set.order_by('-borrow_date')
    context = {'game': game, 'borrows': borrows}
    return render(request, 'board_game_groups/game.html', context)

@login_required
def new_game(request):
    if request.method != 'POST':
        form = GameForm()
    else:
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            form.save()
            return redirect('board_game_groups:games')
    context = {'form': form}
    return render(request, 'board_game_groups/new_game.html', context)

@login_required
def new_borrow(request, game_id):
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        form = BorrowForm()
    else:
        form = BorrowForm(data=request.POST)
        if form.is_valid():
            new_borrow = form.save(commit=False)
            new_borrow.game = game
            new_borrow.borrower = request.user
            new_borrow.save()
            return redirect('board_game_groups:game', game_id=game_id)

    context = {'game': game, 'form': form}
    return render(request, 'board_game_groups/new_borrow.html', context)

@login_required
def edit_borrow(request, borrow_id):
    borrow = Borrow.objects.get(id=borrow_id)
    game = borrow.game

    if request.method != 'POST':
        form = BorrowForm(instance=borrow)
    else:
        form = BorrowForm(instance=borrow, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_groups:game', game_id=game.id)
    
    context = {'borrow': borrow, 'game': game, 'form': form}
    return render(request, 'board_game_groups/edit_borrow.html', context)

@login_required
def edit_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = GameForm(instance=game)
    else:
        form = GameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('board_game_groups:game', game_id=game.id)
    
    context = {'game': game, 'form': form}
    return render(request, 'board_game_groups/edit_game.html', context)