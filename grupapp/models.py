from django.db import models

# Create your models here.
class MakeTeam(models.Model):
    date = models.DateField()
    week = models.IntegerField()
    team1 = models.TextField()
    team2 = models.TextField()
    team3 = models.TextField()
    team4 = models.TextField()
    team5 = models.TextField()  