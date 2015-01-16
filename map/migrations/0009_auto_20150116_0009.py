# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_auto_20150115_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predio',
            name='photo',
            field=models.ImageField(default=b'media/no-imager.jpg', upload_to=b'media'),
            preserve_default=True,
        ),
    ]
