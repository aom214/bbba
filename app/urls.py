from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='home'),
    path('sign/',views.sign,name='signup'),
    path('login/',views.loginn,name='login'),
    path('logoutt/',views.logoutt,name='logout'),
    path('AllTeams/',views.myteams,name='teams'),
    path('base/',views.base,name='base'),
    path('AllTeams/<str:team_namee>/',views.players,name='players'),
    path('bookticket/<str:match_id>/',views.bookticket,name="bookticket"),
    path('pointstable/',views.poi,name='points Table'),
    path('register/',views.registerteam,name='register'),
    path('ticketcounter/',views.ticketcounter,name='ticketcounter'),
    path('delete/<str:product_id>/',views.removeproduct,name='ticketcounter'),
    path('<str:previous_id>/desc/',views.previousdesc,name='matchdesc'),
    path('<str:team_namee>/addplayers/',views.regplayers,name='addplayers'),
    path('addplayerform/<str:team_nam>/',views.addplayerform,name='addplayersform'),
    path('previous/',views.previousmat,name='previousmatches'),
    path('deleteplayer/<str:team_name>/<str:player_id>',views.deleteplayer,name='deleteplayer'),
    path('profile/',views.profil,name='profile'),
    path('search/',views.search,name='search'),
]