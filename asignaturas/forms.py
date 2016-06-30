from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import SelectDateWidget
from datetime import datetime
from .models import calendar



class courseForm(forms.ModelForm):
    class Meta:
		model = calendar
		fields = ('cursoAcademico', 'inicioPrimerCuatrimestreDia', 'inicioPrimerCuatrimestreMes', 'finPrimerCuatrimestreDia', 'finPrimerCuatrimestreMes', 'inicioSegundoCuatrimestreDia', 'inicioSegundoCuatrimestreMes', 'finSegundoCuatrimestreDia', 'finSegundoCuatrimestreMes')
    def __init__(self, *args, **kwargs):
        super(courseForm, self).__init__(*args, **kwargs)
        self.fields['cursoAcademico'].widget.attrs.update({'class': 'form-input'})
        self.fields['inicioPrimerCuatrimestreDia'].widget.attrs.update({'class': 'form-input'})
        self.fields['inicioPrimerCuatrimestreMes'].widget.attrs.update({'class': 'form-input'})
        self.fields['finPrimerCuatrimestreDia'].widget.attrs.update({'class': 'form-input'})
        self.fields['finPrimerCuatrimestreMes'].widget.attrs.update({'class': 'form-input'})
        self.fields['inicioSegundoCuatrimestreDia'].widget.attrs.update({'class': 'form-input'})
        self.fields['inicioSegundoCuatrimestreMes'].widget.attrs.update({'class': 'form-input'})
        self.fields['finSegundoCuatrimestreDia'].widget.attrs.update({'class': 'form-input'})
        self.fields['finSegundoCuatrimestreMes'].widget.attrs.update({'class': 'form-input'})