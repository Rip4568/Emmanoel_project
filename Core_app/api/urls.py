from django.urls import path
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register('perfil-modelviewsets',viewsets.PerfilModelViewSet, basename='perfil-modelviewset')
router.register('perfil-viewsets',viewsets.PerfilViewSet,basename='perfil-viewsets')
router.register('perfil-nickname-exists', viewsets.NicknameExistsViewSet, basename='nickname-exists')
router.register('user-viewset', viewsets.UserViewSet, basename='user-viewset')
router.register('postagem-modelviewset', viewsets.PostagemModelViewSet, basename='postagem-modelviewset')
router.register('grupo-modelviewsets', viewsets.GrupoModelViewSet, basename='grupo-modelviewsets')
router.register('participantes-modelviewsets',viewsets.ParticipanteModelViewSet, basename='participantes-modelviewsets')
router.register('mensagem-participante-modelviewsets', viewsets.MensagemParticipanteModelViewSet, basename='mensagem-participante-modelviewsets')
router.register('solicitacao-amizade-modelviewsets', viewsets.SolicitacaoAmizadeModelViewSet, basename='solicitacao-amizade-modelviewsets')

urlpatterns = [
  path('login/', viewsets.CustomLoginView.as_view(), name='login'),
] + router.urls