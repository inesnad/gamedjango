from django.http import HttpResponse
from django.http import Http404
from catalog.models import Game
from django.template import loader


def index(request):
    # request games
    try:
        games = Game.objects.filter(available=True).order_by('-created_at')[:3]
    except Game.DoesNotExist:
        raise Http404("Game does not exist")
    template = loader.get_template('catalog/index.html')
    context = {
        'games': games
    }
    return HttpResponse(template.render(context,request=request))


