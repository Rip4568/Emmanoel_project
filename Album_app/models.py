from django.db import models

from Perfil_app.models import Perfil

""" tratar todas as fotos enviadas no request.data """

class Album(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("Album")
        verbose_name_plural = ("Albuns")

    def __str__(self):
        return f'{self.perfil}'

class Imagem(models.Model):
    #imagem = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    imagem = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Imagem")
        verbose_name_plural = ("Imagens")

    def __str__(self):
        return f'{self.album}'