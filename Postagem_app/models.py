from django.urls import reverse
from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _

from Album_app.models import Album
from Perfil_app.models import Perfil

class Postagem(models.Model):
    fotos = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name='fotos')
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, blank=True, null=True, related_name='minhas_postagens')
    like = models.IntegerField(_("Like"), blank=True, null=True, default=0)
    dislike = models.IntegerField(_("Dislike"), blank=True, null=True, default=0)
    texto = models.TextField(_("Texto qualquer da postagem"),blank=True, null=True)
    data_postagem = models.DateTimeField(_("Data da postagem"),auto_now_add=True, blank=False, null=True)

    class Meta:
        verbose_name = ("Postagem")
        verbose_name_plural = ("Postagens")

    def __str__(self):
        return f'{self.perfil}'

class Comentario(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios')
    comentario = models.TextField(_("Comentario feito na postagem, atualmente sem limite de caracteres"))


    class Meta:
        verbose_name = _("Comentario Postagem")
        verbose_name_plural = _("Comentarios em Postagens")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("comentariopostagem_detail", kwargs={"pk": self.pk})
