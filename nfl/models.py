from django.db import models
from colorfield.fields import ColorField

# Models are Python classes that represent objects in the database
# A model is the single, definitive source of information about your data. It contains the essential
# fields and behaviors of the data you’re storing. Generally, each model maps to a single database table.


class Team(models.Model):
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    conference = models.CharField(max_length=3)
    division = models.CharField(max_length=20)
    primary_color = ColorField(default="#FFFFFF")
    secondary_color = ColorField(default="#FFFFFF")
    tertiary_color = ColorField(default="#FFFFFF")
    team_instagram_url = models.URLField(max_length=100, default="#")
    team_page_url = models.URLField(max_length=100, default="#")
    team_twitter_url = models.URLField(max_length=100, default="#")

    def __str__(self):
        return self.name
