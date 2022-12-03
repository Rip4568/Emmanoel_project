from django.urls import path
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register('perfil-modelviewsets',viewsets.PerfilModelViewSet)
router.register('perfil-viewsets',viewsets.PerfilViewSet,basename='perfil-viewsets')
router.register('perfil-nickname-exists', viewsets.NicknameExistsViewSet, basename='nickname-exists')
router.register('user-viewset', viewsets.UserViewSet, basename='user-viewset')
router.register('postagem-modelviewset', viewsets.PostagemModelViewSet, basename='postagem-modelviewset')

urlpatterns = [
] + router.urls