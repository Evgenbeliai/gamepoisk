from django.shortcuts import render, get_object_or_404
from .models import Game, Screenshot


def start(request):
    GAMES = Game.objects.all()
    qurey = request.GET.get('q')
    if qurey:
        filter_games = [game for game in GAMES if qurey.lower() in game.title.lower()]
    else:

        filter_games = GAMES
    
    contex = {'games':filter_games}
    return render(request, 'games/game.html', contex)
def gameinf(request, gameid):
    games = get_object_or_404(Game, pk = gameid)
    screenshot = Screenshot.objects.filter(game_id = gameid)
    return render(request, 'games/gameinf.html',{'games':games,
                                                 'scrinshot':screenshot})
# Create your views here.
