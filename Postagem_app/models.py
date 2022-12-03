from django.db import models

from Album_app.models import Album
from Perfil_app.models import Perfil

class Postagem(models.Model):
    fotos = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True)
    texto = models.CharField(max_length=255, blank=False, null=True)

    class Meta:
        verbose_name = ("Postagem")
        verbose_name_plural = ("Postagens")

    def __str__(self):
        return f'{self.perfil}'
