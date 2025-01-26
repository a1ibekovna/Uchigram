
from rest_framework import generics, permissions
from django_filters import rest_framework as filters

from .models import Category, Publication
from .serializers import CategorySerializer, PublicationSerializer
from .permissions import IsOwnerorReadonly
from .filters import CategoryFilter, PublicationFilter

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CategoryFilter

class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PublicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [IsOwnerorReadonly]
