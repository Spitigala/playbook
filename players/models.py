from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sport = models.CharField(max_length=20)
    league = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s %s %s %s %s' % (self.first_name, self.last_name, self.sport, self.league, self.team)