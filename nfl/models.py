from django.db import models
from colorfield.fields import ColorField


class Team(models.Model):
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    conference = models.CharField(max_length=3)
    division = models.CharField(max_length=20)
    primary_color = ColorField(default="#FFFFFF")
    secondary_color = ColorField(default="#FFFFFF")
    tertiary_color = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.name
