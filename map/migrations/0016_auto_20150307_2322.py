# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0015_auto_20150307_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nacimiento',
            old_name='identificador',
            new_name='nacimiento',
        ),
        migrations.AlterField(
            model_name='predio',
            name='altura_max',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='altura_min',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='clase_agrologica',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='clima',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='ecosistema',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='relieve',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='suelos',
            field=models.CharField(max_length=25, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='zona_de_vida',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
