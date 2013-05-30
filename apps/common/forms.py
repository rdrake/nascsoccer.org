from haystack.forms import SearchForm
from haystack.query import SearchQuerySet

class ForgivingSearchForm(SearchForm):
    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        #return SearchQuerySet().autocomplete(text_ngram=self.cleaned_data["q"])
        return SearchQuerySet().raw_search(self.cleaned_data["q"])
