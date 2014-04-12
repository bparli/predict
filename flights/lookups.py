#lookups.py for Django-selectable
from .models import AirportsRefTable
from selectable.registry import registry
from selectable.base import ModelLookup, LookupBase

class AirportsLookup(ModelLookup):
    model = AirportsRefTable
    search_fields = ('unique_airport_id__icontains', 'airport_code__icontains', 'airport_name__icontains')

    def get_item_label(self,item):
        return u"%s - %s" % (item.airport_code, item.airport_name)

    def get_item_value(self, item):
        #return item.unique_airport_id
        return u"%s - %s" % (item.airport_code, item.airport_name)

    def get_item_id(self,item):
        return item.unique_airport_id

registry.register(AirportsLookup)