# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='solisitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_recepcion', models.DateTimeField(verbose_name=b'date published')),
                ('nombre', models.CharField(max_length=200)),
                ('municipio', models.CharField(max_length=20)),
                ('actividad', models.CharField(max_length=80)),
                ('monto', models.DecimalField(max_digits=11, decimal_places=2)),
                ('sector', models.CharField(max_length=80)),
                ('programa', models.CharField(max_length=200)),
                ('analista', models.CharField(max_length=80)),
                ('estatus', models.CharField(max_length=20)),
                ('fecha_asignacion', models.DateTimeField(verbose_name=b'date published')),
                ('comite', models.CharField(max_length=80)),
                ('fecha_comite', models.DateTimeField(verbose_name=b'date published')),
                ('recibio_expediente', models.CharField(max_length=80)),
                ('observaciones', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
