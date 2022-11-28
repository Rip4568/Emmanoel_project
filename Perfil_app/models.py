from django.db import models

class Perfil(models.Model):
    nome = models.CharField(max_length=128, blank=True, null=True)
    data_inserido = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural = ("Perfis")

    def __str__(self):
        return self.nome