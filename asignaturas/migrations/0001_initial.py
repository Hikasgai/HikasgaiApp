# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-21 14:39
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('codigo', models.IntegerField()),
                ('nombreCompleto', models.CharField(max_length=50)),
                ('curso', models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo'), ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto')], max_length=10)),
                ('idioma', models.CharField(choices=[('eu', 'Euskera'), ('en', 'Ingles'), ('es', 'Castellano')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AsignaturaAnno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plazasSolicitadas', models.IntegerField(default=0)),
                ('anno', models.IntegerField()),
                ('creditosMinimos', models.IntegerField(default=0)),
                ('plazasOcupadas', models.IntegerField(default=0)),
                ('plazasMaximas', models.IntegerField(default=0)),
                ('cuatrimestre', models.CharField(choices=[('1', 'Primero'), ('2', 'Segundo')], max_length=10)),
                ('diaHorarioAgrupado', models.CharField(blank=True, choices=[('L', 'Lunes'), ('M', 'Martes'), ('X', 'Miercoles'), ('J', 'Jueves'), ('V', 'Viernes')], max_length=10)),
                ('eventos', jsonfield.fields.JSONField(blank=True)),
                ('horarios', jsonfield.fields.JSONField(blank=True)),
                ('descripcion', models.CharField(max_length=1000)),
                ('enlaceGuia', models.URLField(blank=True)),
                ('colorEvento', models.CharField(blank=True, max_length=8)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.Asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=140)),
                ('fechaCreacion', models.DateField(blank=True, default=datetime.date.today)),
                ('fechaUltimaModificacion', models.DateField(blank=True, default=datetime.date.today)),
                ('puntuacion', models.IntegerField(default=0)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CursoAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicioCuatrimestreUno', models.DateField(blank=True, default=datetime.date.today)),
                ('inicioCuatrimestreDos', models.DateField(blank=True, default=datetime.date.today)),
                ('finCuatrimestreUno', models.DateField(blank=True, default=datetime.date.today)),
                ('finCuatrimestreDos', models.DateField(blank=True, default=datetime.date.today)),
                ('fiestas', jsonfield.fields.JSONField(blank=True)),
                ('especiales', jsonfield.fields.JSONField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('universidad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.Facultad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeGustaComentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(default=0)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.Comentario')),
                ('valorador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MeGustaTarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=140)),
                ('titulo', models.CharField(max_length=50)),
                ('HFin', models.TimeField(blank=True)),
                ('HInicio', models.TimeField(blank=True)),
                ('puntuacion', models.IntegerField(default=0)),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ValoracionAsignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.IntegerField(default=0)),
                ('argumento', models.CharField(blank=True, max_length=140)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.AsignaturaAnno')),
                ('creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='megustatarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.Tarea'),
        ),
        migrations.AddField(
            model_name='megustatarea',
            name='valorador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cursoacademico',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asignaturas.Facultad'),
        ),
    ]
