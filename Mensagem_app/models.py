from django.db import models
from Perfil_app.models import Perfil
class Chat(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    #perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING)
    """ melhor forma sera um enviou e outro recebeu
    após isso criar um campo para mensagem_lida para saber se a conversa no chat foi lida """
    
    class Meta:
        verbose_name = ("Chat")
        verbose_name_plural = ("Chats")

    def __str__(self):
        return f'conversa entre: {self.perfil1} , {self.perfil2}'


class Mensagem(models.Model):
    sender = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField(max_length=255)
    when = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = ("mensagem")
        verbose_name_plural = ("mensagens")

    def __str__(self):
        return f'mensagem de {self.perfil} para {self.chat.perfil2}'