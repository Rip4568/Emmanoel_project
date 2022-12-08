# Generated by Django 4.1.3 on 2022-12-08 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Perfil_app', '0006_alter_perfil_nick_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoAmizade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=128, verbose_name='')),
                ('status', models.CharField(choices=[('aceito', 'aceito'), ('pendente', 'pendente'), ('rejeitado', 'rejeitado')], max_length=255)),
                ('de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_de_min', to='Perfil_app.perfil')),
                ('para', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_para_mim', to='Perfil_app.perfil')),
            ],
            options={
                'verbose_name': 'SolicitacaoAmizade',
                'verbose_name_plural': 'SolicitacaoAmizades',
            },
        ),
    ]
