from django.contrib import admin


from .models import Game, Console, Player, Result

admin.site.register(Game)
admin.site.register(Console)
admin.site.register(Player)
admin.site.register(Result)