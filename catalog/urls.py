from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('list/', views.listing, name='list'),
    url(r'^(?P<game_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    path('results/<int:game_id>/', views.listingResultbyGame, name='listresult'),
    path('addResult/', views.addResult, name='addResult'),
]