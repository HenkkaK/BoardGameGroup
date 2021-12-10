from django.shortcuts import render

def index(request):
    return render(request, 'board_game_groups/index.html')