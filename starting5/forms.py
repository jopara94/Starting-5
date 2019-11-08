from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'logo_url', 'summary',)

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'nba_team', 'photo_url', 'team')