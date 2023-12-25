# Generated by Django 4.1.3 on 2023-01-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil_app', '0003_amigos_perfil_amigos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='amigos',
            field=models.ManyToManyField(blank=True, to='Perfil_app.perfil'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nick_name',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True),
        ),
    ]