from django.http import HttpResponse
from django.http import Http404
from catalog.models import Game
from django.template import loader


def listing(request):
    # request games
    try:
        games = Game.objects.filter(available=True)
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    template = loader.get_template('catalog/games.html')
    context = {
        'games': games
    }
    return HttpResponse(template.render(context,request=request))


