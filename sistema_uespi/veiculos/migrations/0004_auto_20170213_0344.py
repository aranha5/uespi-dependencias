# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0003_auto_20170213_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculos',
            name='data_revisao',
            field=models.DateField(verbose_name='Data da ultima revisão(DD/MM/YYYY)'),
        ),
    ]
