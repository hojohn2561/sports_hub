# Generated by Django 3.2.6 on 2021-08-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_instagram_url',
            field=models.URLField(default='#', max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='team_page_url',
            field=models.URLField(default='#', max_length=100),
        ),
        migrations.AddField(
            model_name='team',
            name='team_twitter_url',
            field=models.URLField(default='#', max_length=100),
        ),
    ]
