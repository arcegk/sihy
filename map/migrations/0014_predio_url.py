# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0013_auto_20150307_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='predio',
            name='url',
            field=models.URLField(default=b''),
            preserve_default=True,
        ),
    ]
