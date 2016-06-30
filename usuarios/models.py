from __future__ import unicode_literals
from django.db import models
from datetime import date
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Perfil(models.Model):
    #choices
    GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
    )

    RANGO = (
        ('N', 'Novato'),
        ('E', 'Estudiante'),
        ('B', 'Becario'),
        ('P', 'Pelota')
    )
    #Validador
    gmail_regex = RegexValidator(regex=r'(^[a-zA-Z0-9_.+-]+@gmail.com+$)', message="Tiene que ser una cuenta de Google")

    #Relacionar el modelo de usuario
    usuario = models.OneToOneField(User, models.CASCADE, related_name='perfil')
    #Campos del Perfil
    genero = models.CharField(max_length=1, choices=GENERO, blank=True)
    nacimiento = models.DateField(blank=True, null=True)
    avatar = models.ImageField(blank=True)
    fechaRegistro = models.DateField(default=date.today, blank=True)
    karma = models.IntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)]) #Rango 0-100
    rango = models.CharField(max_length=1, choices=RANGO, default='E')
    cuentaGmail = models.CharField(validators=[gmail_regex], blank=True, max_length=15)

    def __str__(self):
        return self.usuario.username
    class Meta:
        ordering = ('id', )

class Profesor(Perfil):
    #Atributos
    despacho = models.IntegerField(default=0, blank=True)


class Alumno(Perfil):
    CURSO = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto')
    )
    creditos = models.IntegerField(default=0, blank=True)
    notaMedia = models.FloatField(null=True, blank=True)
    curso = models.CharField(max_length=1, choices=CURSO)
    especialidad = models.CharField(max_length=50, blank=True)

class ContactoWeb(models.Model):
    #Atributos
    nombre = models.CharField(max_length=50, blank=True)
    url = models.URLField(blank=True)
    usuario = models.ForeignKey(User)
