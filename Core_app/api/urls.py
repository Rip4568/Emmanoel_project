from django.urls import path
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register('perfil-modelviewsets',viewsets.PerfilModelViewSet)
router.register('perfil-viewsets',viewsets.PerfilViewSet,basename='asdasd')
router.register('perfil-nickname-exists', viewsets.NicknameExistsViewSet, basename='nickname-exists')

urlpatterns = [
] + router.urls