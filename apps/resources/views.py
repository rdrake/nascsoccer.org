from django.views.generic import DetailView, ListView

from .models import Park, Location

class ParkList(ListView):
  model = Park

class ParkDetailView(DetailView):
  model = Park

class LocationList(ListView):
  model = Location

class LocationDetailView(DetailView):
  model = Location
