from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from .models import Alumno, Profesor

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-input'})
        self.fields['email'].widget.attrs.update({'class': 'form-input'})
        self.fields['password'].widget.attrs.update({'class': 'form-input'})

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ('genero', 'nacimiento', 'avatar', 'cuentaGmail', 'creditos', 'notaMedia', 'curso', 'especialidad')
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-input'})
        self.fields['genero'].widget.attrs.update({'class': 'form-input'})
        self.fields['avatar'].widget.attrs.update({'class': 'inputfile'})

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ('genero', 'nacimiento', 'avatar', 'despacho', 'cuentaGmail')
    def __init__(self, *args, **kwargs):
        super(ProfesorForm, self).__init__(*args, **kwargs)
        self.fields['nacimiento'].widget.attrs.update({'class': 'form-input'})
        self.fields['genero'].widget.attrs.update({'class': 'form-input'})
        self.fields['avatar'].widget.attrs.update({'class': 'inputfile'})

