# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 03:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20170207_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.IntegerField(max_length=12, unique=True, verbose_name='CPF')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=2)),
                ('endereco', models.CharField(max_length=50, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=20, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2)),
                ('cep', models.IntegerField(null=True, verbose_name='CEP')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=12, unique=True)),
                ('razao_social', models.CharField(max_length=50, null=True)),
                ('nome_fantasia', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cnpj',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='user',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='user',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='user',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nome_fantasia',
        ),
        migrations.RemoveField(
            model_name='user',
            name='razao_social',
        ),
        migrations.RemoveField(
            model_name='user',
            name='sexo',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True, verbose_name='Usuário'),
        ),
        migrations.AddField(
            model_name='pessoajuridica',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pessoafisica',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]