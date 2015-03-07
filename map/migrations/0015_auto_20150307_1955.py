# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0014_predio_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='predio',
            old_name='temperatura',
            new_name='temperatura_promedio',
        ),
        migrations.AddField(
            model_name='predio',
            name='altura_max',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='altura_min',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='clase_agrologica',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='clima',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='ecosistema',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='relieve',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='suelos',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='zona_de_vida',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='observaciones',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
