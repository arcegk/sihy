# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_auto_20150116_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nacimiento',
            name='cabecera_municipal',
        ),
        migrations.RemoveField(
            model_name='nacimiento',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='nacimiento',
            name='topo_especificacion',
        ),
        migrations.RemoveField(
            model_name='nacimiento',
            name='vegetable_photo',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='predio',
            name='presion_antropica',
        ),
        migrations.RemoveField(
            model_name='nacimiento',
            name='color',
            

        ),
        migrations.AlterField(
            model_name='predio',
            name='corregimiento',
            field=models.CharField(max_length=25, choices=[(b'ARROYOHONDO', b'ARROYOHONDO'), (b'DAPA', b'DAPA'), (b'MULALO', b'MULAL\xc3\x93'), (b'EL PEDREGAL', b'EL PEDREGAL'), (b'SAN MARCOS', b'SAN MARCOS'), (b'SANTA IN\xc3\x89S', b'SANTA IN\xc3\x89S'), (b'YUMBILLO', b'YUMBILLO'), (b'LA OLGA', b'LA OLGA'), (b'LA BUITRERA', b'LA BUITRERA'), (b'MONTA\xc3\x91ITAS', b'MONTA\xc3\x91ITAS')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='cuenca',
            field=models.CharField(max_length=25, choices=[(b'KEY', b'VALUE')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='sub_cuenca',
            field=models.CharField(max_length=25, choices=[(b'KEY', b'VALUE'), (b'AA', b'BB')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='vereda',
            field=models.CharField(max_length=25, choices=[(b'ARROYOHONDO', b'ARROYOHONDO'), (b'XIXALOA', b'XIXALOA'), (b'MIRAVALLE DAPA', b'MIRAVALLE DAPA'), (b'ALTO DAPA', b'ALTO DAPA'), (b'MEDIO DAPA', b'MEDIO DAPA'), (b'PILAS DAPA', b'PILAS DAPA'), (b'RINC\xc3\x93N DAPA', b'RINC\xc3\x93N DAPA'), (b'EL PEDREGAL', b'EL PEDREGAL'), (b'FILO Y LAGUNA', b'FILO Y LAGUNA'), (b'MULALO ', b'MULAL\xc3\x93 '), (b'PLATANARES', b'PLATANARES'), (b'PASO DE LA TORRE', b'PASO DE LA TORRE'), (b'EL HIGUER\xc3\x93N', b'EL HIGUER\xc3\x93N'), (b'SAN MARCOS', b'SAN MARCOS'), (b'MANGA VIEJA', b'MANGA VIEJA'), (b'MIRAVALLE NORTE', b'MIRAVALLE NORTE'), (b'SANTA IN\xc3\x89S', b'SANTA IN\xc3\x89S'), (b'EL CHOCHO', b'EL CHOCHO'), (b'TELECOM', b'TELECOM'), (b'YUMBILLO', b'YUMBILLO'), (b'SALAZAR', b'SALAZAR'), (b'LA OLGA', b'LA OLGA'), (b'LA BUITRERA', b'LA BUITRERA'), (b'MONTA\xc3\x91ITAS ', b'MONTA\xc3\x91ITAS '), (b'SAN JOS\xc3\x89', b'SAN JOS\xc3\x89'), (b'EL PLACER', b'EL PLACER')]),
            preserve_default=True,
        ),
    ]
