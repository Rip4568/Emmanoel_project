# Generated by Django 4.1.3 on 2022-12-03 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil_app', '0005_alter_perfil_nick_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nick_name',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
    ]