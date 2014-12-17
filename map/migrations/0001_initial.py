# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nacimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'')),
                ('vegetable_photo', models.ImageField(upload_to=b'')),
                ('caudal', models.FloatField(default=0.0)),
                ('ph', models.FloatField(default=0.0)),
                ('color', models.CharField(max_length=25, choices=[(b'key', b'value')])),
                ('turbiedad', models.FloatField(default=0.0)),
                ('dureza', models.FloatField(default=0.0)),
                ('sulfatos', models.FloatField(default=0.0)),
                ('nitratos', models.FloatField(default=0.0)),
                ('temperatura', models.FloatField(default=0.0)),
                ('dbo', models.FloatField(default=0.0)),
                ('solidos', models.FloatField(default=0.0)),
                ('dqo', models.FloatField(default=0.0)),
                ('coliformes', models.FloatField(default=0.0)),
                ('cabecera_municipal', models.CharField(max_length=25, choices=[(b'key', b'value')])),
                ('topo_especificacion', models.CharField(max_length=25, choices=[(b'key', b'value')])),
                ('altura', models.IntegerField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catastro', models.CharField(max_length=25)),
                ('escritura', models.CharField(max_length=25)),
                ('area', models.IntegerField()),
                ('corregimiento', models.CharField(max_length=25, choices=[(b'aa', b'bb'), (b'key', b'value')])),
                ('vereda', models.CharField(max_length=25, choices=[(b'key', b'value'), (b'aa', b'bb')])),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('cuenca', models.CharField(max_length=25, choices=[(b'KEY', b'value')])),
                ('sub_cuenca', models.CharField(max_length=25, choices=[(b'key', b'value'), (b'aa', b'bb')])),
                ('temperatura', models.FloatField(default=0.0)),
                ('presion_antropica', models.CharField(max_length=25, choices=[(b'key', b'value')])),
                ('photo', models.ImageField(upload_to=b'')),
                ('via_pavimentada', models.FloatField(default=0.0)),
                ('via_destapada', models.FloatField(default=0.0)),
                ('via_trocha', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nacimiento',
            name='predio',
            field=models.ForeignKey(to='map.Predio'),
            preserve_default=True,
        ),
    ]
