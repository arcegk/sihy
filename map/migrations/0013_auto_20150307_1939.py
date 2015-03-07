# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0012_auto_20150221_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='fecha_acta',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='numero_acta',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
    ]
