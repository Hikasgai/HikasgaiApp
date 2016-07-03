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


class calendar(models.Model):
    DIAS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31')
    )
    MESES = (
        ('1', 'Enero'),
        ('2', 'Febrero'),
        ('3', 'Marzo'),
        ('4', 'Abril'),
        ('5', 'Mayo'),
        ('6', 'Junio'),
        ('7', 'Julio'),
        ('8', 'Agosto'),
        ('9', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre')
    )

    CURSOS = (
        ('2016/2017', '16/17'),
        ('2017/2018', '17/18')
    )

    cursoAcademico = models.IntegerField(choices=CURSOS, blank=True)
    inicioPrimerCuatrimestreDia = models.IntegerField(choices=DIAS, blank=True)
    inicioPrimerCuatrimestreMes = models.IntegerField(choices=MESES, blank=True)
    finPrimerCuatrimestreDia = models.IntegerField(choices=DIAS, blank=True)
    finPrimerCuatrimestreMes = models.IntegerField(choices=MESES, blank=True)
    inicioSegundoCuatrimestreDia = models.IntegerField(choices=DIAS, blank=True)
    inicioSegundoCuatrimestreMes = models.IntegerField(choices=MESES, blank=True)
    finSegundoCuatrimestreDia = models.IntegerField(choices=DIAS, blank=True)
    finSegundoCuatrimestreMes = models.IntegerField(choices=MESES, blank=True)
