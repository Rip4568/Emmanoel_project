# Generated by Django 4.1.3 on 2022-12-09 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Perfil_app', '0001_initial'),
        ('Grupo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='participante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='Perfil_app.perfil'),
        ),
        migrations.AddField(
            model_name='mensagemparticipante',
            name='de',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensagens_enviadas', to='Grupo_app.participante'),
        ),
        migrations.AddField(
            model_name='mensagemparticipante',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mensagens', to='Grupo_app.grupo'),
        ),
    ]