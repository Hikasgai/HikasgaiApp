from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime



CURSOS = (
<<<<<<< HEAD
    ('2016/2017', '2016/2017'),
    ('2017/2018', '2017/2018')
=======
    ('16/17', '2016/2017'),
    ('17/18', '2017/2018')
>>>>>>> 2cf1c25a035faf05836569a22a47b26ed52061c8
)


class courseForm(forms.Form):
    cursoAcademico = forms.ChoiceField(choices=CURSOS)
<<<<<<< HEAD
    inicioPrimerCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    finPrimerCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    inicioSegundoCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
    finSegundoCuatrimestre = forms.DateField(widget=forms.SelectDateWidget())
=======
    inicioCuatrimestreUno = forms.DateField(widget=forms.SelectDateWidget())
    finCuatrimestreUno = forms.DateField(widget=forms.SelectDateWidget())
    inicioCuatrimestreDos = forms.DateField(widget=forms.SelectDateWidget())
    finCuatrimestreDos = forms.DateField(widget=forms.SelectDateWidget())
>>>>>>> 2cf1c25a035faf05836569a22a47b26ed52061c8
