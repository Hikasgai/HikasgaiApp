# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-22 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asignaturas', '0002_facultad_especialidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asignaturaanno',
            name='horarios',
        ),
        migrations.RemoveField(
            model_name='cursoacademico',
            name='especiales',
        ),
        migrations.RemoveField(
            model_name='cursoacademico',
            name='fiestas',
        ),
    ]
