# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculos',
            name='data_revisao',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]