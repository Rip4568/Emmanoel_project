from django.urls import path, include

from .api import urls

app_name = 'Core_app'

urlpatterns = [
    path('', include(urls), name='api')
]