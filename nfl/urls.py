from django.urls import path
from . import views

# nfl/
urlpatterns = [
    path('', views.index, name="nfl_index"),
    path('teams', views.teams, name="nfl_teams")
]
