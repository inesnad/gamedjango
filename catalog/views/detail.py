from django.http import HttpResponse
from django.http import Http404
from catalog.models import Game
from django.template import loader



def detail(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
        consoles = " ".join([console.name for console in game.consoles.all()])
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    template = loader.get_template('catalog/detail_game.html')
    context = {
        'game': game,
        'consoles':consoles
    }
    return HttpResponse(template.render(context,request=request))

