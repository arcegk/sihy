# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0019_auto_20150323_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='predio',
            name='fecha_adquisicion',
            field=models.CharField(default='', max_length=30, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predio',
            name='plan_manejo',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predio',
            name='valor',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='vendedor',
            field=models.CharField(default='', max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
