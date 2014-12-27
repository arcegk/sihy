# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20141227_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='nacimiento',
            name='identificador',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='nombre',
            field=models.CharField(default=b'', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='presion_antropica',
            field=models.CharField(max_length=25, choices=[(b'1', b'val1'), (b'2', b'val2'), (b'3', b'val3'), (b'4', b'val4'), (b'5', b'val5')]),
            preserve_default=True,
        ),
    ]
