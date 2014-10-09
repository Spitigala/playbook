from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sport = models.CharField(max_length=20)
    league = models.CharField(max_length=100)
    team = models.CharField(max_length=100)