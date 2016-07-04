from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import course_form, diasNoLectivos_form, diasSinClase_form, semanaHorarioEspecial_form, semanasExcluidas_form, diasCambiados_form
from asignaturas.views import ContactWizard

urlpatterns = [
#	url(r'^calendario', views.crear_calendario, name='calendario'),
    url(r'^courses$', views.user_courses, name='courses'),
    url(r'^disenarcalendario$', views.disenar_calendario, name='disenar_calendario'),
    url(r'^formwizard$', ContactWizard.as_view([course_form,diasNoLectivos_form,diasSinClase_form,semanaHorarioEspecial_form,semanasExcluidas_form,diasCambiados_form]),name='formwizard')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
