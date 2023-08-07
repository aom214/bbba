from django.contrib import admin
from app.models import upcoming,addplayers,teams,points,regteam,register_players,previous,matchCart,profile
# Register your models here.
admin.site.register(upcoming)
admin.site.register(addplayers)
admin.site.register(teams)
admin.site.register(register_players)
admin.site.register(regteam)
admin.site.register(points)
admin.site.register(previous)
admin.site.register(matchCart)
admin.site.register(profile)