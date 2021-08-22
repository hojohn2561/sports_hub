from django.contrib import admin
from.models import Team


class TeamAdmin (admin.ModelAdmin):
    list_display = ('id', 'city', 'name')


admin.site.register(Team, TeamAdmin)
