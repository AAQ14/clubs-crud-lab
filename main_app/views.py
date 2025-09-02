# from django.shortcuts import render, redirect
# from .models import Club

# FBV:

# Create your views here.
# get all clubs
# def all_clubs(req):
#     clubs = Club.objects.all()
#     return render(req, "clubs-list.html", {'clubs':clubs})


# def create_club(req):
#     if req.method == 'POST':
#         name = req.POST.get('name')
#         country = req.POST.get('country')
#         is_there_match = req.POST.get('is_there_match') =="on"
#         print("this is: ",is_there_match)
#         match_time = req.POST.get('match_time')
#         players_num = req.POST.get('players_num')

#         Club.objects.create(name = name, country=country, is_there_match = is_there_match, match_time=match_time, players_num=players_num)
#         return redirect('all-clubs')
#     return render(req, "clubs-form.html")


# def clubs_details(req, id):
#     club = Club.objects.get(id=id)
#     return render(req, "clubs-details.html", {'club': club})

# def update_club(req,id):
#    club = Club.objects.get(id=id)
#    if req.method == 'POST':
#         club.name = req.POST.get('name')
#         club.country = req.POST.get('country')
#         club.is_there_match = req.POST.get('is_there_match')
#         print("this is: ",club.is_there_match)
#         club.match_time = req.POST.get('match_time')
#         club.players_num = req.POST.get('players_num')
#         club.save()
#         return redirect('all-clubs')
   
#    return render(req, "clubs-form.html", {'club': club})

# def delete_club(req, id):
#       Club.objects.get(id=id).delete()
#       return redirect('all-clubs')


# CBV:
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Club, Match
from .forms import ClubForm, MatchForm
from django.db.models import Q

class ClubListView(ListView):
    model = Club
    template_name = "clubs/clubs-list.html"
    context_object_name = 'clubs'


class ClubDetailView(DetailView):    
    model = Club
    template_name = 'clubs/clubs-details.html'
    context_object_name = 'club'
    print(Match.objects.all())

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['matches'] = Match.objects.filter(Q(team1=self.object) | Q(team2=self.object))
        return ctx

class ClubCreateView(CreateView):
    model = Club
    form_class = ClubForm
    template_name = 'clubs/clubs-form.html'

    def get_success_url(self):
        return reverse("club-details", kwargs={"pk": self.object.pk})
    
class ClubUpdateView(UpdateView):
    model = Club
    template_name = 'clubs/clubs-form.html'
    form_class = ClubForm
    success_url = "/"
    pk_url_kwarg = 'club_id'

class ClubDeleteView(DeleteView):
    model = Club
    success_url = reverse_lazy('all-clubs')


class MatchListView(ListView):
    model= Match
    template_name = 'matches/matches-list.html'
    context_object_name = 'matches'

class MatchCreateView(CreateView):
    model= Match
    form_class = MatchForm
    template_name = 'matches/match-form.html'
    success_url = reverse_lazy('all-matches')

    def get_success_url(self):
        return reverse("match-details", kwargs={"pk": self.object.pk})
    
class MatchDetailView(DetailView):
    model = Match
    template_name = 'matches/match-details.html'
    context_object_name = 'match'

class MatchUpdateView(UpdateView):
    model = Match
    template_name = 'matches/match-form.html'
    form_class = MatchForm
    success_url= reverse_lazy('all-matches')

class MatchDeleteView(DeleteView):
    model = Match
    success_url = reverse_lazy('all-matches')
