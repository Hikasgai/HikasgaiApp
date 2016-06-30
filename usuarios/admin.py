from django.contrib import admin
from .models import Alumno, Profesor

# Register your models here.
@admin.register(Alumno)
class AdminAlumno(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )

@admin.register(Profesor)
class AdminProfesor(admin.ModelAdmin):
    list_display = ('id',)
    list_filter = ('id', )
