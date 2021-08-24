from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.shortcuts import redirect



def addResult(request):
    if request.user.groups.filter(name='Player'):
        template = loader.get_template('catalog/addResult.html')
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return HttpResponse(template.render(request=request))


