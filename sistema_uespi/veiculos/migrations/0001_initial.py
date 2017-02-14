# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_veiculo', models.CharField(blank=True, choices=[('O', 'Ônibus'), ('M', 'Microônibus'), ('C', 'Carro')], max_length=2)),
                ('placa', models.CharField(max_length=8, verbose_name='Placa do veículo')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernanbuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2)),
                ('cidade', models.CharField(max_length=20, verbose_name='Cidade')),
                ('chassi', models.CharField(max_length=18, verbose_name='Chassi')),
                ('cor', models.CharField(max_length=11, verbose_name='Cor')),
                ('marca_modelo', models.CharField(max_length=20, verbose_name='Marca/Modelo')),
                ('situacao', models.CharField(blank=True, choices=[('D', 'Disponível'), ('R', 'Reservado'), ('E', 'Em manutenção'), ('A', 'Alugado')], max_length=2)),
            ],
        ),
    ]
