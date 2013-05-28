import csv
import sys
import os
import pytz

from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")

from apps.schedule.models import Game, Team, AgeGroup, Competition
from apps.resources.models import Location

from django.utils import timezone

age_group_str = sys.argv[1].split("/")[-1].replace(".csv", "")
competition_str = sys.argv[1].split("/")[-2]

age_group = AgeGroup.objects.get(slug=age_group_str)
competition = Competition.objects.get(slug=competition_str)

current_tz = tzinfo=timezone.get_current_timezone()

with open(sys.argv[1], "rU") as csvfile:
    reader = csv.reader(csvfile, dialect="excel")

    for row in reader:
        datetime_str = "%s %s" % (row[0], row[1])
        home_team_str = row[2].strip()
        away_team_str = row[4].strip()
        location_str = row[6].strip().title()

        home_team_score = None
        away_team_score = None

        try:
            # If we can't get the home score, no point in trying to get the
            # away score anyway.
            home_team_score = int(row[3].strip())
            away_team_score = int(row[5].strip())
        except:
            pass

        if location_str.lower() == "mackenzie":
            location_str = "MacKenzie"

        if home_team_str.lower() == "mackenzie":
            home_team_str = "MacKenzie"
        
        if away_team_str.lower() == "mackenzie":
            away_team_str = "MacKenzie"

        if location_str.lower() == "mclaughlin park":
            location_str = "McLaughlin Park"

        result = datetime.strptime(datetime_str, "%Y-%m-%d %I:%M %p")
        result = current_tz.localize(result)
        result = result.astimezone(pytz.UTC)

        if location_str == "":
            location = None
        else:
            location = Location.objects.get(name=location_str)

        if home_team_str.lower() == "1st place":
            home = None
        else:
            home = Team.objects.get(age_group=age_group, name=home_team_str)

        bye = False

        if away_team_str.lower() == "2nd place":
            away = None
        else:
            if "bye" in away_team_str.lower():
                away = None
                bye = True
            else:
                away = Team.objects.get(age_group=age_group, name=away_team_str)

        if sys.argv[2] == "commit":
            g = Game(when=result, competition=competition, age_group=age_group, home_team=home, home_score=home_team_score, away_team=away, away_score=away_team_score, location=location, bye=bye)
            g.save()
