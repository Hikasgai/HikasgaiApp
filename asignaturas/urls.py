from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import course_form, diasNoLectivos_form, diasSinClase_form, semanaHorarioEspecial_form, semanasExcluidas_form, diasCambiados_form

urlpatterns = [
#	url(r'^calendario', views.crear_calendario, name='calendario'),
    url(r'^courses$', views.user_courses, name='courses'),
    url(r'^crearcalendario$', views.crear_calendario, name='crear_calendario'),
    url(r'^editarcalendario$', views.editar_calendario, name='editar_calendario'),
    url(r'^diasnolectivos$', views.dias_no_lectivos, name='diasnolectivos'),
    url(r'^diassinclase$', views.dias_sin_clase, name='diassinclase'),
    url(r'^periodoshorarioespecial$', views.periodos_horario_especial, name='periodoshorarioespecial'),
    url(r'^semanaexcluida$', views.semanas_excluidas, name='semana_excluida'),
    url(r'^intercambiodias$', views.intercambio_dias, name='intercambiodias'),
    url(r'^quitardiasnolectivos$', views.quitar_dias_no_lectivos, name='quitardiasnolectivos'),
    url(r'^quitardiassinclase$', views.quitar_dias_sin_clase, name='quitardiassinclase'),
    url(r'^descargarcalendario$', views.descargar_calendario, name='descargarcalendario'),
    url(r'^iniciofinal$', views.inicio_final, name='iniciofinal'),
    url(r'^asignaturas$', views.asignaturas, name='asignaturas')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
