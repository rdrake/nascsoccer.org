from django.views.generic import DetailView, ListView

from .models import Item

class ItemListView(ListView):
    model = Item

class ItemDetailView(DetailView):
    model = Item
