from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime

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
class courseForm1(forms.Form):
    cursoAcademico = forms.ChoiceField(choices=CURSOS)
    inicioPrimerCuatrimestre = forms.DateField(widget=forms.TextInput())
    inicioPrimerCuatrimestre.widget.attrs.update({'class': 'datepicker'})

    finPrimerCuatrimestre = forms.DateField(widget=forms.TextInput())
    finPrimerCuatrimestre.widget.attrs.update({'class': 'datepicker'})

    inicioSegundoCuatrimestre = forms.DateField(widget=forms.TextInput())
    inicioSegundoCuatrimestre.widget.attrs.update({'class': 'datepicker'})

    finSegundoCuatrimestre = forms.DateField(widget=forms.TextInput())
    finSegundoCuatrimestre.widget.attrs.update({'class': 'datepicker'})

# Definicion de la Segunda pagina del formulario
# Aqui se recoge informacion secundaria como:
# Dias periodicos din clase, fines de semana, etc
# Dias puntuales sin clase
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class courseForm2(forms.Form):
    diasSemanalesNoLectivos1 = forms.ChoiceField(choices=DIASEMANA)
    diasSemanalesNoLectivos2 = forms.ChoiceField(choices=DIASEMANA)
    fechaDiaSinClase1 = forms.DateField(widget=forms.TextInput())
    fechaDiaSinClase1.widget.attrs.update({'class': 'datepicker'})
    motivoDiasSinClase1 = forms.ChoiceField(choices=MOTIVOSFIESTAS)
    fechaDiaSinClase2 = forms.DateField(widget=forms.TextInput())
    fechaDiaSinClase2.widget.attrs.update({'class': 'datepicker'})
    motivoDiasSinClase2 = forms.ChoiceField(choices=MOTIVOSFIESTAS)

# Definicion de la tercera pagina del formulario
# Aqui se recoge informacion secundaria como:
# Periodos de horario especial
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class courseForm3(forms.Form):
    motivoSemanasHorarioEspecial1 = forms.ChoiceField(choices=MOTIVOSESPECIAL)
    fechaISemanasHorarioEspecial1 = forms.DateField(widget=forms.TextInput())
    fechaISemanasHorarioEspecial1.widget.attrs.update({'class': 'datepicker'})
    fechaFSemanasHorarioEspecial1 = forms.DateField(widget=forms.TextInput())
    fechaFSemanasHorarioEspecial1.widget.attrs.update({'class': 'datepicker'})

    motivoSemanasHorarioEspecial2 = forms.ChoiceField(choices=MOTIVOSESPECIAL)
    fechaISemanasHorarioEspecial2 = forms.DateField(widget=forms.TextInput())
    fechaISemanasHorarioEspecial2.widget.attrs.update({'class': 'datepicker'})
    fechaFSemanasHorarioEspecial2 = forms.DateField(widget=forms.TextInput())
    fechaFSemanasHorarioEspecial2.widget.attrs.update({'class': 'datepicker'})

# Definicion de la cuarta pagina del formulario
# Aqui se recoge informacion terciara como:
# Semanas excluidas, Intercambiodeias
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class courseForm4(forms.Form):
    motivoSemanasExcluidas1 = forms.ChoiceField(choices=MOTIVOSEXCLUIDAS)
    fechaISemanasExcluidas1 = forms.DateField(widget=forms.TextInput())
    fechaISemanasExcluidas1.widget.attrs.update({'class': 'datepicker'})

    motivoSemanasExcluidas2 = forms.ChoiceField(choices=MOTIVOSEXCLUIDAS)
    fechaISemanasExcluidas2 = forms.DateField(widget=forms.TextInput())
    fechaISemanasExcluidas2.widget.attrs.update({'class': 'datepicker'})

    diaOriginal1 = forms.DateField(widget=forms.TextInput())
    diaOriginal1.widget.attrs.update({'class': 'datepicker'})
    diaporQueSeCambia1 = forms.ChoiceField(choices=DIASEMANA)

    diaOriginal2 = forms.DateField(widget=forms.TextInput())
    diaOriginal2.widget.attrs.update({'class': 'datepicker'})
    diaporQueSeCambia2 = forms.ChoiceField(choices=DIASEMANA)
