from haystack import indexes
from models import Player

class PlayerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    last_name = indexes.CharField(model_attr='last_name')

    def get_model(self):
        return Player

    def index_queryset(self, using=None):
        return self.get_model().objects.all()