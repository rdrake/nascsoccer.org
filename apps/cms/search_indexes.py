from haystack import indexes

from .models import ExtendedFlatPage

class ExtendedFlatPageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return ExtendedFlatPage
