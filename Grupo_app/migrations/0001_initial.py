# Generated by Django 4.1.3 on 2022-12-09 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='MensagemParticipante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'MensagemGrupo',
                'verbose_name_plural': 'MensagemGrupos',
            },
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingressou_em', models.DateTimeField(auto_now_add=True, null=True)),
                ('administrador', models.BooleanField(blank=True, default=False, null=True)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='Grupo_app.grupo')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
            },
        ),
    ]
