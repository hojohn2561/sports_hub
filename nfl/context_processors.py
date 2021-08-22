from .models import Team

# Info on Custom Context Processors
# https://stackoverflow.com/questions/3900617/access-model-data-from-django-base-template
# https://dev.to/gilbishkosma/custom-context-processors-in-django-3c93


def access_afc_east_teams(request):
    # Context processor must return a dictionary
    return {"afc_east_teams": Team.objects.filter(conference="AFC", division="East")}


def access_afc_west_teams(request):
    return {"afc_west_teams": Team.objects.filter(conference="AFC", division="West")}


def access_afc_north_teams(request):
    return {"afc_north_teams": Team.objects.filter(conference="AFC", division="North")}


def access_afc_south_teams(request):
    return {"afc_south_teams": Team.objects.filter(conference="AFC", division="South")}


def access_nfc_east_teams(request):
    return {"nfc_east_teams": Team.objects.filter(conference="NFC", division="East")}


def access_nfc_west_teams(request):
    return {"nfc_west_teams": Team.objects.filter(conference="NFC", division="West")}


def access_nfc_north_teams(request):
    return {"nfc_north_teams": Team.objects.filter(conference="NFC", division="North")}


def access_nfc_south_teams(request):
    return {"nfc_south_teams": Team.objects.filter(conference="NFC", division="South")}
