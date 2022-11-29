from rest_framework import views,viewsets, status
from rest_framework.views import Response

from Perfil_app.models import Perfil
from .serializers import PerfilModelSerializer

class PerfilAPIView(views.APIView):
    """Esta api retorna todos os perfils, ou cria um novo perfil """
    def get(self, request,format=None):
        perfil = Perfil.objects.all()
        serializer = PerfilModelSerializer(perfil, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, format=None):
        serializer:PerfilModelSerializer = PerfilModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NickNameAllAPIView(views.APIView):
    """ Esta api retorna todos os nicknames """
    def get(self, request, format=None):
        perfis = Perfil.objects.all()
        nickNames:list = []
        for perfil in perfis:
            nickNames.append(perfil.nick_name)
        return Response(nickNames)

class NickNameExists(views.APIView):
    """ Esta api retorna um valor booleano para caso exista ja exista ou não o nickname fornecido """
    def get(self, request, nickname,format=None):
        return Response(Perfil.objects.all().filter(nick_name=nickname).exists())

    
    
class PerfilModelViewSet(viewsets.ModelViewSet):
    serializer_class=PerfilModelSerializer
    queryset = Perfil.objects.all()
    
""" class SnippetList(APIView):
    #List all snippets, or create a new snippet.
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """
    
    
""" class SnippetDetail(APIView):
    #Retrieve, update or delete a snippet instance.
    
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """