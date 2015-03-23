# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0018_auto_20150312_0444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='relieve',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
