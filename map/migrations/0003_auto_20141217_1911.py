# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20141216_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nacimiento',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nacimiento',
            name='vegetable_photo',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
