import requests
import json
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Team
from .forms import ScheduleForm


# A view function is a Python function that takes in an Http request and returns a Http response.
# This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML
# document, or an image, anything that a web browser can display.
# The business logic of handling the requests is done by Django Views, it is their purpose.
# This is why Django supplies the request to the view function, so the code can access the
# request data and choose what actions it should take and which response it should send back
# (even though that specific view doesn't make use of it).

# Parse year and week (hofw, pw1, w1, wc, etc.) into correct format for url
def get_schedule_url(year, week):
    # If preseason week
    if ("pw" in week):
        # Preseason week 1 for espn starts with HOFW
        week_num = int(week.split("pw")[1]) + 1
        print(week_num)
        return "https://www.espn.com/nfl/schedule/_/week/" + \
            str(week_num) + "/year/" + year + "/seasontype/1"
    # If hall of fame weekend
    elif ("hofw" in week):
        return "https://www.espn.com/nfl/schedule/_/week/1/year/" + year + "/seasontype/1"
    # If wild card weekend
    elif ("wc" in week):
        return "https://www.espn.com/nfl/schedule/_/week/1/year/" + year + "/seasontype/3"
    # ================= Have yet to handle years with no week 18 =================
    elif ("w" in week):
        week_num = int(week.split("w")[1])
        print(week_num)
        return "https://www.espn.com/nfl/schedule/_/week/" + \
            str(week_num) + "/year/" + year + "/seasontype/2"
    elif ("dr" in week):
        return "https://www.espn.com/nfl/schedule/_/week/2/year/" + year + "/seasontype/3"
    elif ("cc" in week):
        return "https://www.espn.com/nfl/schedule/_/week/3/year/" + year + "/seasontype/3"
    elif ("pb" in week):
        return "https://www.espn.com/nfl/schedule/_/week/4/year/" + year + "/seasontype/3"
    elif ("sb" in week):
        return "https://www.espn.com/nfl/schedule/_/week/5/year/" + year + "/seasontype/3"


def index(request):
    return render(request, 'nfl/index.html')


def teams(request):
    return render(request, "nfl/teams.html")


def schedule(request):
    year = "2021"
    week = "w1"

    if request.method == 'GET':
        form = ScheduleForm(request.GET)
        if form.is_valid():
            year = form.cleaned_data["year"]
            week = form.cleaned_data["week"]

    url = get_schedule_url(year, week)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # On the html page, game days are located in the divs with the class "table-caption"
    game_day_html_tags = soup.select(".table-caption")
    game_days = [day.getText() for day in game_day_html_tags]
    games_data = {game_day: [] for game_day in game_days}

    # On the html page, tables containing the day's matchups are located in the divs with the class "responsive-table-wrap"
    game_table_containers = soup.select(".responsive-table-wrap")
    for index, game_table_container in enumerate(game_table_containers):
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

                games_data[game_days[index]].append({
                    'home_team': home_team_full_name, 'away_team': away_team_full_name})

    # print(json.dumps(games_data, indent=4))

    # Initialize the form with initial values.
    # Upon submission, page will reload, which will cause form to reset. Setting to initial values to be submitted form values so it updates, and doesn't reset to default.
    return render(request, "nfl/schedule.html", {'schedule_form': ScheduleForm(initial={'year': year, 'week': week}), 'games_data': games_data})


def standings(request):
    return render(request, "nfl/standings.html")


def team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, "nfl/team.html", {'team': team})
