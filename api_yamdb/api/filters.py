from rest_framework import filters

from ..reviews.models import Title


class TitleFilter(filters.FilterSet):
    category = filters.CharFilter(
        field_name='categore__slug',
        lookup_expr='exact'
    )
    genre = filters.CharFilter(
        field_name='genre__slug',
        lookup_expr='exact'
    )
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='contains'
    )
    year = filters.RangeFilter()

    class Meta:
        model = Title
        fields = ('category', 'genre', 'name', 'year')