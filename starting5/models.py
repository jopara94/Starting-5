from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    logo_url = models.TextField()

    def __str__(self):
        return self.team_name

class Player(models.Model):
    name = models.CharField(max_length=100)
    nba_team = models.CharField(max_length=100)
    photo_url = models.TextField()
    # artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title