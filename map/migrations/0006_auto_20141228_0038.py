# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_auto_20141227_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='nombre',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
