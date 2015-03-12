# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0017_auto_20150312_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='protegido',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
