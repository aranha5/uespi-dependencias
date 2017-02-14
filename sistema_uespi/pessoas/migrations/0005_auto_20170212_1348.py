# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_auto_20170212_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoafisica',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Administrador'),
        ),
    ]
