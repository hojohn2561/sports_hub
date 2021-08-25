from django.urls import path
from . import views

# urlpatterns map the url to a view
# nfl/
urlpatterns = [
    path('', views.index, name="nfl_index"),
    path('teams', views.teams, name="nfl_teams"),
    path('standings', views.standings, name="nfl_standings"),
    path('schedule', views.schedule, name="nfl_schedule"),
    path('teams/<int:team_id>', views.team, name="nfl_team")
]
