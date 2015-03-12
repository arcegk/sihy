# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0016_auto_20150307_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='area',
            field=models.FloatField(verbose_name='area (Ha)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='url',
            field=models.URLField(default=b'', blank=True),
            preserve_default=True,
        ),
    ]
