from django.urls import path, include

from .api import urls

app_name = 'Core_app'

urlpatterns = [
    path('api/', include(urls), name='api')
]