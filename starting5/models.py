from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=100, default='My Team Name')
    summary = models.CharField(max_length=100, default='How I Describe My Team')
    logo_url = models.TextField()

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100, default='Player Name')
    nba_team = models.CharField(max_length=100, default='NBA Team')
    photo_url = models.TextField(null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players', default='')

    def __str__(self):
        return self.name