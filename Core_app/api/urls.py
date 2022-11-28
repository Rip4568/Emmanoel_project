from django.urls import path
from . import viewsets

urlpatterns = [
    path('',viewsets.PerfilAPIView.as_view()),
]