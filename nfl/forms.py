from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class ScheduleForm(forms.Form):
    year = forms.ChoiceField(
        choices=[
            ("2021", "2021"),
            ("2020", "2020"),
            ("2019", "2019")
        ]
    )
    week = forms.ChoiceField(
        choices=[
            ("hofw", "Hall of Fame Weekend"),
            ("pw1", "Preseason Week 1"),
            ("pw2", "Preseason Week 2"),
            ("pw3", "Preseason Week 3"),
            ("pw4", "Preseason Week 4"),
            ("w1", "Week 1"),
            ("w2", "Week 2"),
            ("w3", "Week 3"),
            ("w4", "Week 4"),
            ("w5", "Week 5"),
            ("w6", "Week 6"),
            ("w7", "Week 7"),
            ("w8", "Week 8"),
            ("w9", "Week 9"),
            ("w10", "Week 10"),
            ("w11", "Week 11"),
            ("w12", "Week 12"),
            ("w13", "Week 13"),
            ("w14", "Week 14"),
            ("w15", "Week 15"),
            ("w16", "Week 16"),
            ("w17", "Week 17"),
            ("w18", "Week 18"),
            ("wc", "Wild Card"),
            ("dr", "Divisional Round"),
            ("cc", "Conference Championship"),
            ("pb", "Pro Bowl"),
            ("sb", "Super Bowl")
        ]
    )
