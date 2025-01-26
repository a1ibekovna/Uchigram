from django_filters import rest_framework as filters

from .models import Category, Publication

class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Category
        fields = ['name']

class PublicationFilter(filters.FilterSet):
    content = filters.CharFilter(lookup_expr='icontains')
    user = filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    category = filters.CharFilter(field_name='category__name', lookup_expr='icontains')


    class Meta:
        model = Publication
        fields = ['content', 'user', 'category']