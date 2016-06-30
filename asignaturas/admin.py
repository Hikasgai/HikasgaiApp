from django.contrib import admin
from .models import Campus, Facultad, Grado, NivelCurso, Asignatura, GrupoIdioma, Grupo, Tarea, MeGustaTarea, ValoracionAsignatura, Comentario, MeGustaComentario, Logs, SubscripcionGrupo, Matricula

@admin.register(Campus)
class AdminCampus(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo')
    list_filter = ('id', )

@admin.register(Facultad)
class AdminFacultad(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'campus')
    list_filter = ('id', 'campus', )

@admin.register(Grado)
class AdminGrado(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo')
    list_filter = ('id', 'codigo')

@admin.register(NivelCurso)
class AdminNivelCurso(admin.ModelAdmin):
    list_display = ('id', 'curso', 'grado')
    list_filter = ('id', 'curso', )

@admin.register(Asignatura)
class AdminAsignatura(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'curso', 'cuatrimestre')
    list_filter = ('id', 'curso', 'codigo')

@admin.register(GrupoIdioma)
class AdminGrupoIdioma(admin.ModelAdmin):
    list_display = ('id', 'nombreIdioma', 'acronimoAsignatura', 'nombreAsignatura')
    list_filter = ('id', )

@admin.register(Grupo)
class AdminGrupo(admin.ModelAdmin):
    list_display = ('id', 'nombre',)
    list_filter = ('id', )

@admin.register(ValoracionAsignatura)
class AdminValoracionAsignatura(admin.ModelAdmin):
    list_display = ('id', 'valoracion')
    list_filter = ('id',)


@admin.register(Tarea)
class AdminTarea(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor')
    list_filter = ('id',)

@admin.register(MeGustaTarea)
class AdminMeGustaTarea(admin.ModelAdmin):
    list_display = ('id', 'valor', 'autor')
    list_filter = ('id',)

@admin.register(Comentario)
class AdminAsignatura(admin.ModelAdmin):
    list_display = ('id', 'autor', 'puntuacion', 'fechaCreacion')
    list_filter = ('id', 'autor', 'puntuacion', 'fechaCreacion')

@admin.register(MeGustaComentario)
class AdminMeGustaComentario(admin.ModelAdmin):
    list_display = ('id', 'autor', 'comentario')
    list_filter = ('id',)

@admin.register(Logs)
class AdminLogs(admin.ModelAdmin):
    list_display = ('id', 'data')
    list_filter = ('id', )

@admin.register(SubscripcionGrupo)
class AdminSubscripcionGrupo(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'grupo')
    list_filter = ('id', )

@admin.register(Matricula)
class AdminFacultad(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'grupo', 'grado')
    list_filter = ('id', )
