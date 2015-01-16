# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20141228_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='area',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
