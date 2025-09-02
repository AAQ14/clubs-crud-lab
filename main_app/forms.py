from django import forms
from .models import Club, Match

class ClubForm(forms.ModelForm):
    class Meta: 
        model = Club
        fields = ["name", "country", "is_there_match", "players_num"]

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ["team1", "team2", "date", "time", "stadium"]