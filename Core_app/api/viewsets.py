from rest_framework import views,viewsets, status
from django.core.paginator import Paginator
from rest_framework.views import Response

from Perfil_app.models import Perfil
from .serializers import PerfilModelSerializer

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