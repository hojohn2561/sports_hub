from django.shortcuts import render
from django.http import HttpResponse


# The business logic of handling the requests is done by Django Views, it is their purpose.
# This is why Django supplies the request to the view function, so the code can access the
# request data and choose what actions it should take and which response it should send back
# (even though that specific view doesn't make use of it).
def index(request):
    return render(request, 'nfl/index.html')


def teams(request):
    return render(request, "nfl/teams.html")
