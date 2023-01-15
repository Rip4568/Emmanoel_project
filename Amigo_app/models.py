#Amigo_app/models.py

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from Perfil_app.models import Perfil

""" class Amigos(models.Model):
    #usuario1 = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='amigos_usuario1', blank=False,null=True)
    #usuario2 = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='amigos_usuario2', blank=False,null=True)
    data_amizade = models.DateTimeField(auto_now_add=True, blank=False,null=True) """

class SolicitacaoAmizade(models.Model):
    de = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitacao_de_min')
    para = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitacao_para_mim')
    mensagem = models.CharField(_(""), max_length=128, default="Olá, quero ser seu amigo!")
    status = models.CharField(max_length=16, choices=[
        ('pendente','pendente'),
        ('aceito','aceito'),
        ('rejeitado','rejeitado'),
    ])
    

    class Meta:
        verbose_name = _("SolicitacaoAmizade")
        verbose_name_plural = _("SolicitacoesAmizades")

    def __str__(self):
        return f'{self.de} para {self.para}, status: {self.status}'

    def get_absolute_url(self):
        return reverse("SolicitacaoAmizade_detail", kwargs={"pk": self.pk})

