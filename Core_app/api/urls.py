from django.urls import path
from . import viewsets

urlpatterns = [
    path('',viewsets.PerfilAPIView.as_view()),
    path('all-nicknames/',viewsets.NickNameAllAPIView.as_view()),
    path('nickname-exists/<nickname>/',viewsets.NickNameExists.as_view()),
]