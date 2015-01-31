# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20150131_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='nacimiento',
            name='color',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
