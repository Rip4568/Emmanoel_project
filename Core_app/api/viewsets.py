from django.core.paginator import Paginator
from django.contrib.auth.models import User
from rest_framework import views,viewsets, status
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import LoginView
from dj_rest_auth.serializers import LoginSerializer

from Perfil_app.models import Perfil
from Postagem_app.models import Postagem
from Grupo_app.models import Grupo, Participante

from .serializers import (
    PerfilModelSerializer, 
    PostagemModelSerializer, 
    UserModelSerializer, 
    GrupoModelSerializer, 
    ParticipanteModelSerializer
    )

#talvez seja melhor fazer as importações somente pela serilizaers

class CustomLoginView(LoginView):
    def get_response(self):
        orginal_response = super().get_response()
        perfil = Perfil.objects.get(user=self.user)
        mydata = {
            "user": LoginSerializer(self.user).data,
            "perfil": PerfilModelSerializer(perfil).data,
            "postagens": Postagem.objects.filter(perfil=perfil),
            "grupos_participantes": None,
            }
        orginal_response.data.update(mydata)
        return orginal_response

class GrupoModelViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoModelSerializer

class ParticipanteModelViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteModelSerializer

class PostagemModelViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemModelSerializer

class UserViewSet(viewsets.ViewSet):
    """ Retorna uma lista de usuarios ou um usuario em especifico """
    def list(self, request, format=None):
        queryset = User.objects.all()
        serializer = UserModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk, format=None):
        queryset = User.objects.get(pk-pk)
        serializer = UserModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #fazer os restantes das operações de api aqui

class PerfilModelViewSet(viewsets.ModelViewSet):
    """ RESUMO """
    serializer_class = PerfilModelSerializer
    queryset = Perfil.objects.all()

class PerfilViewSet(viewsets.ViewSet):
    """ Esta API retornar uma lista de perfis ou um unico perfil passando o parametro id na url
    EX: /perfil-viewsets/ = retornar todas os perfis
    EX: /perfil-viewsets/<Pk:int>/ = retornar um Perfil passando a primary key (pk) como argumento  """
    def list(self, request):
        queryset = Perfil.objects.all()
        serializer = PerfilModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, format=None):
        queryset = Perfil.objects.get(pk=pk)
        serializer = PerfilModelSerializer(queryset, many=False)
        return Response(serializer.data)


class NicknameExistsViewSet(viewsets.ViewSet):
    """ Esta api retorna um valor booleano caso exista o nickname passado como parametro pela url """
    def list(self, request, format=None):
        #o metodo list tem que aparecer em todos os viewsets para ser registrado
        return Response('passe um argumento para a api')
    def retrieve(self, request, pk, format=None):
        return Response(Perfil.objects.filter(nick_name=pk).exists())

""" 
metodos da classeBased ViewSets
Para exibições de detalhes (com uma chave primária na url), os métodos de solicitação usam o seguinte mapa

    GET- - retrieve(self, request, pk, format=None) | list
    PUT- - update(self, request, pk, format=None)
    PATCH- - partial_update(self, request, pk, format=None)
    DELETE- - destroy(self, request, pk, format=None)
 """