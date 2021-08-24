from django.http import HttpResponse
from catalog.models import Game
import logging


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
        logging.error('Something went wrong!')
    else:
        games = ["<li>{}</li>".format(game.title) for game in games]
        message = """
            Nous avons trouvé les jeux correspondant à votre requête ! Les voici :
            <ul>{}</ul>
        """.format("".join(games))

    return HttpResponse(message)

