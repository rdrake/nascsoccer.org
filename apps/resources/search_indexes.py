from haystack import indexes

from .models import Park, Location

class ParkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")

    def get_model(self):
        return Park

class LocationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr="name")
    location = indexes.LocationField()

    def get_model(self):
        return Location

    def prepare_location(self, obj):
        return "%s,%s" % (obj.lat, obj.lng)
