from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Team, Player
from .forms import TeamForm, PlayerForm

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'starting5/team_list.html', {'teams': teams})

def team_detail(request, pk):
    teams = Team.objects.get(id=pk)
    return render(request, 'starting5/team_detail.html', {'team': team})



def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm()
    return render(request, 'starting5/team_form.html', {'form': form})



def team_edit(request, pk):
    team = Team.objects.get(pk=pk)
    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()
            return redirect('artist_detail', pk=team.pk)
    else:
        form = TeamForm(instance=team)
    return render(request, 'starting5/team_formƒ.html', {'form': form})



def team_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')


def player_list(request):
    players = Player.objects.all()
    return render(request, 'starting5/player_list.html', {'players': players})


def player_detail(request, pk):
    player = Player.objects.get(id=pk)
    return render(request, 'starting5/player_detail.html', {'player': player})



def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=song.pk)
    else:
        form = PlayerForm()
    return render(request, 'starting5/player_form.html', {'form': form})



def player_edit(request, pk):
    player = Player.objects.get(pk=pk)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'starting5/player_form.html', {'form': form})



def player_delete(request, pk):
    Player.objects.get(id=pk).delete()
    return redirect('player_list')