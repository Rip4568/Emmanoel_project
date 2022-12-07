from django.db import models
from Perfil_app.models import Perfil
from django.utils.translation import gettext_lazy as _


class Amigo(models.Model):
    de = models.ForeignKey('FKNAME', on_delete=models.CASCADE)
    para = models.ForeignKey('FKNAME', on_delete=models.CASCADE)
    status_solicitacao = models.CharField(max_length=255, choices=[
        ('aceito','aceito'),
        ('pendente','pendnete'),
        ('rejeitado','rejeitado'),
    ])

    """ METODOS ABAIXO """


    class Meta:
        verbose_name = _("Amigo")
        verbose_name_plural = _("Amigos")

    def __str__(self):
        return self.name

