from rest_framework import serializers, viewsets
from .models import Category, Publication


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = '__all__'
        read_only_fields = ['id', 'user', 'create', 'updates']