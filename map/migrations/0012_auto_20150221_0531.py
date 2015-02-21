# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_nacimiento_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='predio',
            name='fecha_acta',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='numero_acta',
            field=models.CharField(default=b'', max_length=25),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='observaciones',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='predio',
            name='protegido',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='corregimiento',
            field=models.CharField(max_length=25, choices=[(b'ARROYOHONDO', b'ARROYOHONDO'), (b'DAPA', b'DAPA'), (b'MULALO', b'MULAL\xc3\x93'), (b'EL PEDREGAL', b'EL PEDREGAL'), (b'SAN MARCOS', b'SAN MARCOS'), (b'SANTA INES', b'SANTA IN\xc3\x89S'), (b'YUMBILLO', b'YUMBILLO'), (b'LA OLGA', b'LA OLGA'), (b'LA BUITRERA', b'LA BUITRERA'), (b'MONTANITAS', b'MONTA\xc3\x91ITAS')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='cuenca',
            field=models.CharField(max_length=25, choices=[(b'YUMBO', b'YUMBO'), (b'ARROYOHONDO', b'ARROYOHONDO'), (b'CAUCA', b'CAUCA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='sub_cuenca',
            field=models.CharField(max_length=25, choices=[(b'YUMBILLO', b'YUMBILLO'), (b'SANTA INES', b'SANTA IN\xc3\x89S'), (b'LA BUITRERA', b'LA BUITRERA'), (b'MULALO', b'MULAL\xc3\x93'), (b'LA PEREZ', b'LA PEREZ')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='predio',
            name='vereda',
            field=models.CharField(max_length=25, choices=[(b'ARROYOHONDO', b'ARROYOHONDO'), (b'XIXALOA', b'XIXALOA'), (b'MIRAVALLE DAPA', b'MIRAVALLE DAPA'), (b'ALTO DAPA', b'ALTO DAPA'), (b'MEDIO DAPA', b'MEDIO DAPA'), (b'PILAS DAPA', b'PILAS DAPA'), (b'RINCON DAPA', b'RINC\xc3\x93N DAPA'), (b'EL PEDREGAL', b'EL PEDREGAL'), (b'FILO Y LAGUNA', b'FILO Y LAGUNA'), (b'MULALO ', b'MULAL\xc3\x93 '), (b'PLATANARES', b'PLATANARES'), (b'PASO DE LA TORRE', b'PASO DE LA TORRE'), (b'EL HIGUERON', b'EL HIGUER\xc3\x93N'), (b'SAN MARCOS', b'SAN MARCOS'), (b'MANGA VIEJA', b'MANGA VIEJA'), (b'MIRAVALLE NORTE', b'MIRAVALLE NORTE'), (b'SANTA INES', b'SANTA IN\xc3\x89S'), (b'EL CHOCHO', b'EL CHOCHO'), (b'TELECOM', b'TELECOM'), (b'YUMBILLO', b'YUMBILLO'), (b'SALAZAR', b'SALAZAR'), (b'LA OLGA', b'LA OLGA'), (b'LA BUITRERA', b'LA BUITRERA'), (b'MONTANITAS ', b'MONTA\xc3\x91ITAS '), (b'SAN JOSE', b'SAN JOS\xc3\x89'), (b'EL PLACER', b'EL PLACER')]),
            preserve_default=True,
        ),
    ]
