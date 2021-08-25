import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Team

# A view function is a Python function that takes in an Http request and returns a Http response.
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML
# document, or an image, anything that a web browser can display.
# The business logic of handling the requests is done by Django Views, it is their purpose.
# This is why Django supplies the request to the view function, so the code can access the
# request data and choose what actions it should take and which response it should send back
# (even though that specific view doesn't make use of it).


def index(request):
    return render(request, 'nfl/index.html')


def teams(request):
    return render(request, "nfl/teams.html")


def schedule(request):
    response = requests.get(
        "https://www.espn.com/nfl/schedule/_/week/1/year/2021/seasontype/2")
    soup = BeautifulSoup(response.text, "html.parser")

    # On the html page, game days are located in the divs with the class "table-caption"
    game_day_html_tags = soup.select(".table-caption")
    game_days = [day.getText() for day in game_day_html_tags]
    print(game_days)

    # On the html page, tables containing the day's matchups are located in the divs with the class "responsive-table-wrap"
    game_table_containers = soup.select(".responsive-table-wrap")
    for game_table_container in game_table_containers:
        game_tables = game_table_container.select("tbody")

        # Multiple game tables because multiple days where games are played
        for game_table in game_tables:
            # Each game is a row in the table
            games = game_table.select("tr")

            # Get the home/away team for each game
            for game in games:
                # For each game, full team names are defined in abbr title attribute. Find the 2 abbr for the game, and get the title
                home_team_full_name, away_team_full_name = map(
                    lambda team_abbr_tag: team_abbr_tag.attrs["title"], game.findAll("abbr"))

                print(away_team_full_name, "at", home_team_full_name)

    return render(request, "nfl/schedule.html")


def standings(request):
    return render(request, "nfl/standings.html")


def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, "nfl/team.html", {'team': team})
