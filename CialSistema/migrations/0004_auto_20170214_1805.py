# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CialSistema', '0003_auto_20170214_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='operacion',
        ),
        migrations.AddField(
            model_name='operacion',
            name='equipo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CialSistema.Equipo'),
            preserve_default=False,
        ),
    ]
