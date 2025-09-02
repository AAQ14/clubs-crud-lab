from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_there_match = models.BooleanField()
    players_num = models.IntegerField()

    class Meta:
        db_table = 'clubs'

    def __str__(self):
        return f'{self.name}'

class Match(models.Model):
    team1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team1_matches')
    team2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team2_matches')
    date = models.DateField()
    time = models.TimeField()
    stadium = models.CharField(max_length=100)

    class Meta:
        db_table = 'matches'
    
    # def __str__(self):
    #     return f'{self.team1} vs {self.team2}'