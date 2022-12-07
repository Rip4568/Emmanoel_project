from django.urls import path, include

from .api import urls
from . import views

app_name = 'Core_app'

urlpatterns = [
    path('', include(urls), name='api'),
    path('chat/', views.index, name="index"),
    path('chat/lobby/<str:room_name>', views.room, name='room'),
    path('teste/', views.TesteView.as_view(), name='teste'),
]