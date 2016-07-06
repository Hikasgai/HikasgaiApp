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
DIASEMANAL = (
    ('MON', 'Lunes'),
    ('TUE', 'Martes'),
    ('WED', 'Miercoles'),
    ('THU', 'Jueves'),
    ('FRI', 'Viernes'),
    ('SAT', 'Sabado'),
    ('SUN', 'Domingo')
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
    inicioPrimerCuatrimestre = forms.DateField(widget=forms.TextInput(), required='true', input_formats=settings.DATE_INPUT_FORMATS)
    inicioPrimerCuatrimestre.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)

    finPrimerCuatrimestre = forms.DateField(widget=forms.TextInput(), required='true', input_formats=settings.DATE_INPUT_FORMATS)
    finPrimerCuatrimestre.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)

    inicioSegundoCuatrimestre = forms.DateField(widget=forms.TextInput(), required='true', input_formats=settings.DATE_INPUT_FORMATS)
    inicioSegundoCuatrimestre.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)

    finSegundoCuatrimestre = forms.DateField(widget=forms.TextInput(), required='true', input_formats=settings.DATE_INPUT_FORMATS)
    finSegundoCuatrimestre.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)

    def clean(self):
        super(course_form, self).clean()
        if self.is_valid():
            form_data = self.cleaned_data
            if form_data['inicioPrimerCuatrimestre'] > form_data['finPrimerCuatrimestre']:
                self._errors['__all__'] = ["Fechas de incio/fin primer cuatrimestre incorrecta!"]
                del form_data['finPrimerCuatrimestre']
                del form_data['inicioPrimerCuatrimestre']
            elif form_data['inicioSegundoCuatrimestre'] > form_data['finSegundoCuatrimestre']:
                self._errors['__all__'] = ["Fechas de segundo cuatrimestre incorrectas!"]
                del form_data['finSegundoCuatrimestre']
                del form_data['inicioSegundoCuatrimestre']
            elif form_data['inicioSegundoCuatrimestre'] < form_data['finPrimerCuatrimestre']:
                self._errors['__all__'] = ErrorList(["Cuatrimestres solapados!"])
                del form_data['inicioPrimerCuatrimestre']
                del form_data['inicioSegundoCuatrimestre']
            else:
                return form_data

# Aqui se recoge informacion secundaria como:
# Dias periodicos din clase, fines de semana, etc
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class diasNoLectivos_form(forms.Form):
    diasSemanalesNoLectivos = forms.ChoiceField(choices=DIASEMANA)


# Aqui se recoge informacion secundaria como:
# Dias puntuales sin clase
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class diasSinClase_form(forms.Form):
    fechaDiaSinClase = forms.DateField(widget=forms.TextInput(), input_formats=settings.DATE_INPUT_FORMATS)
    fechaDiaSinClase.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)
    motivoDiasSinClase = forms.ChoiceField(choices=MOTIVOSFIESTAS)
 

# Aqui se recoge informacion secundaria como:
# Periodos de horario especial
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class semanaHorarioEspecial_form(forms.Form):
    motivoSemanasHorarioEspecial = forms.ChoiceField(choices=MOTIVOSESPECIAL)
    fechaISemanasHorarioEspecial = forms.DateField(widget=forms.TextInput(), input_formats=settings.DATE_INPUT_FORMATS)
    fechaISemanasHorarioEspecial.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)
    fechaFSemanasHorarioEspecial = forms.DateField(widget=forms.TextInput(), input_formats=settings.DATE_INPUT_FORMATS)
    fechaFSemanasHorarioEspecial.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)


# Aqui se recoge informacion terciara como:
# Semanas excluidas
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class semanasExcluidas_form(forms.Form):
    motivoSemanasExcluidas = forms.ChoiceField(choices=MOTIVOSEXCLUIDAS)
    fechaISemanasExcluidas = forms.DateField(widget=forms.TextInput(), input_formats=settings.DATE_INPUT_FORMATS)
    fechaISemanasExcluidas.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)

# Aqui se recoge informacion terciaria como:
# Dias de horario cambiado
# TODO Adaptar formulario para funcionar dinamicamente, poder anadir campos
class diasCambiados_form(forms.Form):
    diaOriginal = forms.DateField(widget=forms.TextInput(), input_formats=settings.DATE_INPUT_FORMATS)
    diaOriginal.widget.attrs.update({'class': 'datepicker'}, input_formats=settings.DATE_INPUT_FORMATS)
    diaporQueSeCambia = forms.ChoiceField(choices=DIASEMANAL)

