from django_filters import rest_framework as filters
from django_filters import FilterSet

from products.models import Phone


class PhoneFilterSet(FilterSet):
    company = filters.CharFilter(field_name='company', lookup_expr='exact', label='Компания')
    model = filters.CharFilter(field_name='model', lookup_expr='contains')
    color = filters.CharFilter(field_name='color', lookup_expr='contains')
    price = filters.NumberFilter(field_name='price', lookup_expr='lt')
    memory = filters.NumberFilter(method='get_by_memory')

    class Meta:
        model = Phone
        fields = 'company', 'model', 'color', 'price', 'description', 'memory'

    def get_by_memory(self, queryset, name, value):
        result = queryset.filter(memory__size=int(value))
        return result
