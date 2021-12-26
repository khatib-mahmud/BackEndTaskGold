import django_filters

from .models import *

class MobileFilter(django_filters.FilterSet):
    class Meta:
        model = Mobile
        fields = ['Model', 'JAN_Code']
        
        