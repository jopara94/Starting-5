from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('teams/<int:pk>', views.team_detail, name='team_detail'),
    path('teams/new', views.team_create, name='team_create'),
    path('teams/<int:pk>/edit', views.team_edit, name='team_edit'),
    path('teams/<int:pk>/delete', views.team_delete, name='team_delete'),


    path('players', views.player_list, name='player_list'),
    path('players/<int:pk>', views.player_detail, name='player_detail'),
    path('players/new', views.player_create, name='player_create'),
    path('players/<int:pk>/edit', views.player_edit, name='player_edit'),
    path('players/<int:pk>/delete', views.player_delete, name='player_delete')
]