from django.http import HttpResponse
from .models import Game, Console, Player, Result
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth.decorators import permission_required
import logging
from .forms import ResultForm
# ...

def listingResultbyGame(request, game_id):
        results = Result.objects.filter(game=game_id)
        #results = Result.objects.all()
        formatted_results = ["<li>{}</li>".format(result.score) for result in results]
        message = """<ul>{}</ul>""".format("\n".join(formatted_results))
        template = loader.get_template('catalog/resultByGame.html')
        context = {
            'results': results
        }
        return HttpResponse(template.render(context,request=request))

def addResult(request):
    if request.user.groups.filter(name='Player'):
        template = loader.get_template('catalog/addResult.html')
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return HttpResponse(template.render(request=request))

def index(request):
    # request albums
    games = Game.objects.filter(available=True).order_by('-created_at')[:3]
    formatted_games = ["<li>{}</li>".format(game.title) for game in games]
    message = """<ul>{}</ul>""".format("\n".join(formatted_games))
    template = loader.get_template('catalog/index.html')
    context = {
        'games': games
    }
    return HttpResponse(template.render(context,request=request))

def listing(request):
    games = Game.objects.filter(available=True)
    formatted_games = ["<li>{}</li>".format(game.title) for game in games]
    message = """<ul>{}</ul>""".format("\n".join(formatted_games))
    template = loader.get_template('catalog/games.html')
    context = {
        'games': games
    }
    return HttpResponse(template.render(context,request=request))

def detail(request, game_id):
    game = Game.objects.get(pk=game_id)
    consoles = " ".join([console.name for console in game.consoles.all()])
    message = "Le nom du jeu est {}. Il peut être joué sur {}".format(game.title, consoles)
    return HttpResponse(message)

def search(request):
    query = request.GET.get('query')
    if not query:
        games = Game.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        games = Game.objects.filter(title__icontains=query)

    if not games.exists():
        games = Game.objects.filter(consoles__name__icontains=query)

    if not games.exists():
        message = "Nous n'avons trouvé aucun résultat !"
        logger.error('Something went wrong!')
    else:
        games = ["<li>{}</li>".format(game.title) for game in games]
        message = """
            Nous avons trouvé les jeux correspondant à votre requête ! Les voici :
            <ul>{}</ul>
        """.format("".join(games))

    return HttpResponse(message)

