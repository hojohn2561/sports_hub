from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Team


# The business logic of handling the requests is done by Django Views, it is their purpose.
# This is why Django supplies the request to the view function, so the code can access the
# request data and choose what actions it should take and which response it should send back
# (even though that specific view doesn't make use of it).
def index(request):
    return render(request, 'nfl/index.html')


def teams(request):
    return render(request, "nfl/teams.html")


def schedule(request):
    return render(request, "nfl/schedule.html")


def standings(request):
    return render(request, "nfl/standings.html")


def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, "nfl/team.html", {'team': team})
