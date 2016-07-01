from __future__ import unicode_literals
from django.db import models
from django import forms
from datetime import date, datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from jsonfield import JSONField

from django.conf import settings

class Campus(models.Model):
    CAMPUS = (
        ('AR', 'Araba'),
        ('GI', 'Gipuzkoa'),
        ('BI', 'Bizkaia'),
    )
    nombre = models.CharField(max_length=10, choices=CAMPUS)
    codigo = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Facultad(models.Model):
    nombre = models.CharField(max_length=50)
    campus = models.ForeignKey(Campus)
    def __str__(self):
        return self.nombre

class Grado(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=10)
    # {'especialidades': ['xxx', 'yyyy', 'zzz']}
    especialidades = JSONField(blank=True)
    def __str__(self):
        return self.nombre

class NivelCurso(models.Model):
    #Validador para normalizar las fechas
    fecha_regex = RegexValidator(regex=r'((JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC) ([0-2][0-9]|3(0|1)), 20[1-9][0-9])', message="Tiene que seguir el siguiente ejemplo: 'FEB 28, 2016' ")

    curso = models.CharField(max_length=10)
    inicioCuatrimestreUno = models.CharField(validators=[fecha_regex], blank=True, max_length=15)
    inicioCuatrimestreDos = models.CharField(validators=[fecha_regex], blank=True, max_length=15)
    finCuatrimestreUno = models.CharField(validators=[fecha_regex], blank=True, max_length=15)
    finCuatrimestreDos = models.CharField(validators=[fecha_regex], blank=True, max_length=15)
    grado = models.ForeignKey(Grado)

    def __str__(self):
        return self.curso

class Asignatura(models.Model):

    codigo = models.IntegerField()
    cuatrimestre = models.CharField(max_length=10)
    curso = models.ForeignKey(NivelCurso)

    def __str__(self):
        return self.codigo

class GrupoIdioma(models.Model):
    IDIOMA = (
        ('EU', 'Euskera'),
        ('EN', 'Ingles'),
        ('ES', 'Castellano'),
    )
    nombreIdioma = models.CharField(max_length=10, choices=IDIOMA)
    acronimoAsignatura = models.CharField(max_length=10)
    nombreAsignatura = models.CharField(max_length=50)
    asignatura = models.ForeignKey(Asignatura)
    def __str__(self):
        return self.acronimoAsignatura

class DatosTemporales(models.Model):
    grupoIdioma = models.OneToOneField(GrupoIdioma, related_name='datostemporales')
    def __str__(self):
        return self.grupoIdioma

class Grupo(models.Model):
    nombre = models.IntegerField()
    # {
    # 'Examenes': [{''Nombre': xxx, 'Dia': xxx (Tipo DATEJS), 'HInicio': xxx, 'HFin': xxx}, {..}, {..}],
    # 'Clases': [{'Dia': xxx (Tipo DATEJS), 'HInicio': xxx, 'HFin': xxx}, {..}, {..}],
    # 'Tareas': [{'id', xxx, 'Titulo': xxx, 'Descripcion': xxx, 'HFin': xxx, 'Creador': user.id}, {..}, {..}],
    # }
    eventos = JSONField(blank=True)
    datosTemporales = models.ForeignKey(DatosTemporales)
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    descripcion = models.CharField(max_length=140)
    titulo = models.CharField(max_length=50)
    Hora = models.TimeField(auto_now=False, blank=True)
    puntuacion = models.IntegerField(default=0)
    grupo = models.ForeignKey(Grupo)
    autor = models.ForeignKey(User)
    def __str__(self):
        return self.titulo

class ValoracionAsignatura(models.Model):
    valoracion = models.IntegerField(default=0)
    argumento = models.CharField(max_length=140, blank=True)
    asignatura = models.ForeignKey(Asignatura)
    autor = models.ForeignKey(User)
    def __str__(self):
        return self.id


class MeGustaTarea(models.Model):
    valor = models.IntegerField(default=0)
    autor = models.ForeignKey(User)
    tarea = models.ForeignKey(Tarea)
    def __str__(self):
        return self.tarea.titulo

class Comentario(models.Model):
    contenido = models.CharField(max_length=140)
    fechaCreacion = models.DateField(default=date.today, blank=True)
    fechaUltimaModificacion = models.DateField(default=date.today, blank=True)
    puntuacion = models.IntegerField(default=0)
    autor = models.ForeignKey(User)
    grupoIdioma = models.ForeignKey(GrupoIdioma)
    def __str__(self):
        return self.autor.username

class MeGustaComentario(models.Model):
    valor = models.IntegerField(default=0)
    autor = models.ForeignKey(User)
    comentario = models.ForeignKey(Comentario)
    def __str__(self):
        return self.comentario

class Logs(models.Model):
    data = models.CharField(max_length=255)
    grado = models.ForeignKey(Grado)
    usuario = models.ForeignKey(User)
    def __str__(self):
        return self.grado.nombre

class SubscripcionGrupo(models.Model):
    usuario = models.ForeignKey(User)
    grupo = models.ForeignKey(Grupo)
    def __str__(self):
        return self.usuario.username

class Matricula(models.Model):
    usuario = models.ForeignKey(User)
    grupo = models.ForeignKey(Grupo)
    grado = models.ForeignKey(Grado)