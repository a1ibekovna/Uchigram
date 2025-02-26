
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django_filters import rest_framework as filters

from .models import Category, Publication
from .serializers import CategorySerializer, PublicationSerializer
from .permissions import IsOwnerOrReadOnly
from .filter import CategoryFilter, PublicationFilter

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CategoryFilter

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = PublicationFilter


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
