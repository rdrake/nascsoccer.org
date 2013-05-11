import csv
import sys
import os
import pytz

from time import mktime
from datetime import datetime

import parsedatetime as pdt

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule.settings")

from schedule.models import Game, Team, AgeGroup, Location, Competition
from django.utils import timezone

p = pdt.Calendar()

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

    if location_str.lower() == "mackenzie":
      location_str = "MacKenzie"

    if home_team_str.lower() == "mackenzie":
      home_team_str = "MacKenzie"
    
    if away_team_str.lower() == "mackenzie":
      away_team_str = "MacKenzie"

    if location_str.lower() == "mclaughlin park":
      location_str = "McLaughlin Park"

    datetime_str = datetime_str.replace(".", "").replace("-", " ")
    (result, status) = p.parse(datetime_str)

    if status == 3:
      result = datetime.fromtimestamp(mktime(result))
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
        g = Game(when=result, competition=competition, age_group=age_group, home_team=home, away_team=away, location=location, bye=bye)
        g.save()
    else:
      print(age_group.name)
      print(datetime_str)
      raise Exception
