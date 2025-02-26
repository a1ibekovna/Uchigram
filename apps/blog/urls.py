from django.urls import path
from dj_rest_auth.views import LoginView
from .views import PublicationListCreateAPIView, PublicationRetrieveUpdateDestroyAPIView

from . import views

urlpatterns = [
    path('categories/', view=views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>', view=views.CategoryListCreateAPIView.as_view()),
    path('login', LoginView.as_view(), name='login'),
    path('publications/', view=views.PublicationListCreateAPIView.as_view()),
    path('publications/<int:pk>', views.PublicationRetrieveUpdateDestroyAPIView.as_view(), name='publication-detail'),
]

