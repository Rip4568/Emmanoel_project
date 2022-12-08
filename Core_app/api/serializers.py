from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#from django.utils.translation import ugettext_lazy as _

from Perfil_app.models import Perfil
from Postagem_app.models import Postagem
from Grupo_app.models import Grupo, Participante, MensagemParticipante
from Amigo_app.models import SolicitacaoAmizade

class SolicitacaoAmizadeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitacaoAmizade
        fields = '__all__'
class MensagemParticipanteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MensagemParticipante
        fields= '__all__'

class PerfilModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        #fields = ['id', 'name', 'email'] #selecionar os campos para serializar
        fields = '__all__' #selecionar todos os campos

class GrupoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class ParticipanteModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participante
        fields = '__all__'


class PostagemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



""" 
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        
        #Create and return a new `Snippet` instance, given the validated data.
       
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        #Update and return an existing `Snippet` instance, given the validated data.
       
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance """