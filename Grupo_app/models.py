from django.urls import reverse
from django.db import models
from django.utils.translation import gettext_lazy as _

from Perfil_app.models import Perfil


class Grupo(models.Model):
    """ Essa classe Grupo ira definir todos os grupos que irão existir na rede social, bem como os seus respectivos
    participantes seguindo a seguinte logica:
    campos necessarios/obrigatorios para a criação do grupo:
    nome: str[varchar 64]
    criado_em: Date+Time sera criado automaticamente sempre que o grupo for criado
    administrador: pode ser um ou mais de um """
    nome = models.CharField(max_length=64, null=True, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True, null=True)
    foto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _("Grupo")
        verbose_name_plural = _("Grupos")

    def __str__(self):
        return f'{self.nome} criado em: {self.criado_em}'


class Participante(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='participantes', null=True, blank=False)
    participante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='grupos', null=True, blank=True)
    ingressou_em = models.DateTimeField(auto_now_add=True, null=True)
    administrador = models.BooleanField(default=False, blank=True, null=True)

    def remover_participante(self):
        pass

    def adicionar_participante(self):
        pass

    def convidar_participante(self):
        pass
    

    class Meta:
        verbose_name = _("Participante")
        verbose_name_plural = _("Participantes")

    def __str__(self):
        return f'{self.participante} participa de {self.grupo}'