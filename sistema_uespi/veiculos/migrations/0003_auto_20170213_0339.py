# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0002_veiculos_data_revisao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculos',
            name='data_revisao',
            field=models.DateField(),
        ),
    ]
