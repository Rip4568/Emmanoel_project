import random
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Perfil(models.Model):
    """ blank = pode ser vazio no formulario
    null = deve ou não ser preenchido ao acessar o django-admin """
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)
    nome_completo = models.CharField(max_length=128, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    data_nascimento = models.DateField(auto_now_add=False, blank=True, null=True)
    nick_name = models.CharField(max_length=12, unique=True, blank=True,null=True)
    sexo = models.CharField(max_length=16, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    #futuramente alterar para ImageField
    foto = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural = ("Perfis")

    def __str__(self):
        return f'{self.user} - {self.nick_name}'


#sempre que um usuario for cadastrado com sucesso, crie um perfil
@receiver(post_save, sender=User)
def perfil_post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance, nick_name=random.randint(9,999))

#essa linha abaixo talvez não seja necessario
#pois a funcao do create em objects ja cria e salva no bd
@receiver(post_save, sender=User)
def perfil_post_save_receiver(sender, instance, **kwargs):
    instance.perfil.save()
