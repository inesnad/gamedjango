from django.http import HttpResponse
from catalog.models import Result
from django.template import loader

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


