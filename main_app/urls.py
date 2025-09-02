from django.urls import path
from . import views

urlpatterns = [
   # path('', views.all_clubs, name='all-clubs'),
   # path('new-club/', views.create_club, name='new-club'),
   # path('club-details/<int:id>/', views.clubs_details, name='club-details'),
   # path('update-club/<int:id>/', views.update_club, name='update-club'),
   # path('delete-club/<int:id>/', views.delete_club, name='delete-club'),
   
   path('', views.ClubListView.as_view(), name='all-clubs'),
   path('clubs/<int:pk>/', views.ClubDetailView.as_view(), name='club-details'),
   path('clubs/new/', views.ClubCreateView.as_view(), name='clubs-new'),
   path('clubs/update/<int:club_id>/', views.ClubUpdateView.as_view(), name='clubs-update'),
   path('clubs/delete/<int:pk>/', views.ClubDeleteView.as_view(), name='delete-club'),

   path('matches/', views.MatchListView.as_view(), name='all-matches'),
   path('matches/new/', views.MatchCreateView.as_view(), name='match-new'),
   path('matches/<int:pk>/', views.MatchDetailView.as_view(), name='match-details'),
   path('matches/update/<int:pk>/', views.MatchUpdateView.as_view(), name='update-match'),
   path('matches/delete/<int:pk>/', views.MatchDeleteView.as_view(), name='delete-match'),

]