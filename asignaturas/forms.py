from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime



CURSOS = (
    ('16/17', '2016/2017'),
    ('17/18', '2017/2018')
)


class courseForm(forms.Form):
    cursoAcademico = forms.ChoiceField(choices=CURSOS)
    inicioCuatrimestreUno = forms.DateField(widget=forms.SelectDateWidget())
    finCuatrimestreUno = forms.DateField(widget=forms.SelectDateWidget())
    inicioCuatrimestreDos = forms.DateField(widget=forms.SelectDateWidget())
    finCuatrimestreDos = forms.DateField(widget=forms.SelectDateWidget())
