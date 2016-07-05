from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from django.conf import settings

CURSOS = (
    ('2016/2017', '16/17'),
    ('2017/2018', '17/18')
)
DIASEMANA = (
    ('MO', 'Lunes'),
    ('TU', 'Martes'),
    ('WE', 'Miercoles'),
    ('TH', 'Jueves'),
    ('FR', 'Viernes'),
    ('SA', 'Sabado'),
    ('SU', 'Domingo')
)
MOTIVOSFIESTAS = (
    ('FiestaNacional', 'Fiesta nacional'),
    ('FiestaAutonomica','Fiesta autonomica'),
    ('FiestaLocal','Fiesta local'),
    ('HorarioNoPresencial','No presencial')
)
MOTIVOSESPECIAL = (
    ('HorarioAgrupado', 'Horario agrupado'),
    ('FinDeTrabajos','Fin de trabajos'),
    ('Examenes','Examenes')
)
MOTIVOSEXCLUIDAS = (
    ('Pascua', 'Semana de Pascua'),
    ('Puente','Puente'),
    ('Navidad','Navidad')
)
#  Definicion de la pagina del formulario
#  Aqui se recoge la informacion mas basica del curso academico
#  Ano del curso academico, fechas de inicio e fin de cuatrimestres
class course_form(forms.Form):
    cursoAcademico = forms.ChoiceField(choices=CURSOS)
    inicioPrimerCuatrimestre = forms.DateField(widget=forms.TextInput(), required='false')
    inicioPrimerCuatrimestre.widget.attrs.update({'class': 'datepicker'})

    finPrimerCuatrimestre = forms.DateField(widget=forms.TextInput(), required='false')
    finPrimerCuatrimestre.widget.attrs.update({'class': 'datepicker'})

    inicioSegundoCuatrimestre = forms.DateField(widget=forms.TextInput(), required='false')
    inicioSegundoCuatrimestre.widget.attrs.update({'class': 'datepicker'})

    finSegundoCuatrimestre = forms.DateField(widget=forms.TextInput(), required='false')
    finSegundoCuatrimestre.widget.attrs.update({'class': 'datepicker'})

# Aqui se recoge informacion secundaria como:
# Dias periodicos din clase, fines de semana, etc
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class diasNoLectivos_form(forms.Form):
    diasSemanalesNoLectivos = forms.ChoiceField(choices=DIASEMANA)


# Aqui se recoge informacion secundaria como:
# Dias puntuales sin clase
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class diasSinClase_form(forms.Form):
    fechaDiaSinClase = forms.DateField(widget=forms.TextInput())
    fechaDiaSinClase.widget.attrs.update({'class': 'datepicker'})
    motivoDiasSinClase = forms.ChoiceField(choices=MOTIVOSFIESTAS)
 

# Aqui se recoge informacion secundaria como:
# Periodos de horario especial
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class semanaHorarioEspecial_form(forms.Form):
    motivoSemanasHorarioEspecial = forms.ChoiceField(choices=MOTIVOSESPECIAL)
    fechaISemanasHorarioEspecial = forms.DateField(widget=forms.TextInput())
    fechaISemanasHorarioEspecial.widget.attrs.update({'class': 'datepicker'})
    fechaFSemanasHorarioEspecial = forms.DateField(widget=forms.TextInput())
    fechaFSemanasHorarioEspecial.widget.attrs.update({'class': 'datepicker'})


# Aqui se recoge informacion terciara como:
# Semanas excluidas
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class semanasExcluidas_form(forms.Form):
    motivoSemanasExcluidas = forms.ChoiceField(choices=MOTIVOSEXCLUIDAS)
    fechaISemanasExcluidas = forms.DateField(widget=forms.TextInput())
    fechaISemanasExcluidas.widget.attrs.update({'class': 'datepicker'})

# Aqui se recoge informacion terciaria como:
# Dias de horario cambiado
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class diasCambiados_form(forms.Form):
    diaOriginal = forms.DateField(widget=forms.TextInput())
    diaOriginal.widget.attrs.update({'class': 'datepicker'})
    diaporQueSeCambia = forms.ChoiceField(choices=DIASEMANA)

