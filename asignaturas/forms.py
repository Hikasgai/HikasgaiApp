from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime



CURSOS = (
    ('2016/2017', '2016/2017'),
    ('2017/2018', '2017/2018')
)


class courseForm(forms.Form):
    cursoAcademico = forms.ChoiceField(choices=CURSOS)
    inicioPrimerCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    finPrimerCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    inicioSegundoCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    finSegundoCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
