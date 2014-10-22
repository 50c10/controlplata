# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solisitudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solisitud',
            name='fecha_asignacion',
            field=models.DateField(verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='solisitud',
            name='fecha_comite',
            field=models.DateField(verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='solisitud',
            name='fecha_recepcion',
            field=models.DateField(),
        ),
    ]
