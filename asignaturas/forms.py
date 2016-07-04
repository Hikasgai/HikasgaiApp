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
    ('FRI', 'Viernes'),
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
    inicioPrimerCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    finPrimerCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    inicioSegundoCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    finSegundoCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())

# Definicion de la Segunda pagina del formulario
# Aqui se recoge informacion secundaria como:
# Dias periodicos din clase, fines de semana, etc
# Dias puntuales sin clase
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class courseForm2(forms.Form):
    diasSemanalesNoLectivos1 = forms.ChoiceField(choices=DIASEMANA)
    diasSemanalesNoLectivos2 = forms.ChoiceField(choices=DIASEMANA)
    fechaDiaSinClase1 = forms.DateField(widget=forms.SelectDateWidget())
    motivoDiasSinClase1 = forms.ChoiceField(choices=MOTIVOSFIESTAS)
    fechaDiaSinClase2 = forms.DateField(widget=forms.SelectDateWidget())
    motivoDiasSinClase2 = forms.ChoiceField(choices=MOTIVOSFIESTAS)

# Definicion de la tercera pagina del formulario
# Aqui se recoge informacion secundaria como:
# Periodos de horario especial
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class courseForm3(forms.Form):
    motivoSemanasHorarioEspecial1 = forms.ChoiceField(choices=MOTIVOSESPECIAL)
    fechaISemanasHorarioEspecial1 = forms.DateField(widget=forms.SelectDateWidget())
    fechaFSemanasHorarioEspecial1 = forms.DateField(widget=forms.SelectDateWidget())

    motivoSemanasHorarioEspecial2 = forms.ChoiceField(choices=MOTIVOSESPECIAL)
    fechaISemanasHorarioEspecial2 = forms.DateField(widget=forms.SelectDateWidget())
    fechaFSemanasHorarioEspecial2 = forms.DateField(widget=forms.SelectDateWidget())

# Definicion de la cuarta pagina del formulario
# Aqui se recoge informacion terciara como:
# Semanas excluidas, Intercambiodeias
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class courseForm4(forms.Form):
    motivoSemanasExcluidas1 = forms.ChoiceField(choices=MOTIVOSEXCLUIDAS)
    fechaISemanasExcluidas1 = forms.DateField(widget=forms.SelectDateWidget())

    motivoSemanasExcluidas2 = forms.ChoiceField(choices=MOTIVOSEXCLUIDAS)
    fechaISemanasExcluidas2 = forms.DateField(widget=forms.SelectDateWidget())

    diaOriginal1 = forms.DateField(widget=forms.SelectDateWidget())
    diaporQueSeCambia1 = forms.ChoiceField(choices=DIASEMANA)

    diaOriginal2 = forms.DateField(widget=forms.SelectDateWidget())
    diaporQueSeCambia2 = forms.ChoiceField(choices=DIASEMANA)
