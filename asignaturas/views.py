from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from lib.calendar import mainCalendar
from lib.ehudata import mainData
from .forms import course_form, diasNoLectivos_form, diasSinClase_form, semanaHorarioEspecial_form, semanasExcluidas_form, diasCambiados_form
from formtools.wizard.views import SessionWizardView

# El siguiente metodo especifica lo que debe suceder cuando
# todos los formularios han sido subidos y comprobados
class ContactWizard(SessionWizardView):
    def done(self, form_list,form_dict, **kwargs):
        #
        return render_to_response('asignaturas/mostrar_calendario.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get_template_names(self):
        return ['asignaturas/wizardForm.html']
    """
    def get_form(self, step=None, data=None, files=None):
        form = super(ContactWizard, self).get_form(step, data, files)

        # determine the step if not given
        if step is None:
            step = self.steps.current

        if step == "0":
            loan_sessions = self.request.session.get('loan_sessions', None)
            if loan_sessions != None:
                loan_sessions = pickle.loads(self.request.session['loan_sessions'])
            else:
                loan_sessions = []

            loan_choices = []
            for loan_session in loan_sessions:
                loan_choice = (loan_session['number'], loan_session['name'])
                loan_choices.append(loan_choice)

            ##Pass the data when initing the form, which is the POST
            form = course_form()
        return form
        """
@login_required(login_url='/login')
def user_courses(request):
	return render(request, 'asignaturas/courses.html')

#def course_detail(request):
#	return render(request, 'asignaturas/course_detail.html')
@csrf_exempt
def crear_calendario(request):
	if request.method == 'GET':
		return render(request, 'asignaturas/disenar_calendario.html', {'course_form' : course_form()})
	else:
		resultados = request.POST
		calendarFile = mainCalendar.createCalendarJson(resultados)
        request.session['json'] = json.loads(calendarFile)

        return HttpResponseRedirect("/editarcalendario")

@csrf_exempt
def editar_calendario(request):

    curso = request.session['json']['cursoAcademico']
    fic1 = request.session['json']['inicioCuatrimestreUno']
    fic2 = request.session['json']['inicioCuatrimestreDos']
    ffc1 = request.session['json']['finCuatrimestreUno']
    ffc2 = request.session['json']['finCuatrimestreDos']
    dnl = request.session['json']['diasSemanalesNoLectivos']
    dsc = request.session['json']['diasSinClase']
    phe = request.session['json']['periodosHorarioEspecial']
    se = request.session['json']['semanasExcluidas']
    intd = request.session['json']['intercambioDias']

    """
        'diasSinClase':[],
        'periodosHorarioEspecial':[],
        'semanasExcluidas':[],
        'intercambioDias':[]
    """

    return render(request, 'asignaturas/editar_calendario.html', {'intd':intd,'phe':phe, 'se':se,'dsc':dsc,'dnl':dnl, 'curso' : curso, 'fic1': fic1, 'ffc1': ffc1, 'fic2':fic2, 'ffc2':ffc2, 'diasNoLectivos_form':diasNoLectivos_form(), 'diasSinClase_form':diasSinClase_form(), 'semanaHorarioEspecial_form':semanaHorarioEspecial_form(), 'diasCambiados_form':diasCambiados_form(), 'semanasExcluidas_form':semanasExcluidas_form()})


def dias_no_lectivos(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/editarcalendario')
	else:
		resultados = request.POST
		js = mainCalendar.anadirDiasNoLectivos(resultados, request.session['json'])
		request.session['json'] = js
		
		return HttpResponseRedirect("/editarcalendario")



def dias_sin_clase(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/editarcalendario')
	else:
		resultados = request.POST
		js = mainCalendar.anadirDiasSinClase(resultados, request.session['json'])
		request.session['json'] = js
		
		return HttpResponseRedirect("/editarcalendario")



def periodos_horario_especial(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/editarcalendario')
	else:
		resultados = request.POST
		js = mainCalendar.anadirPeriodosHorarioEspecial(resultados, request.session['json'])
		request.session['json'] = js
		
		return HttpResponseRedirect("/editarcalendario")

def semanas_excluidas(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/editarcalendario')
	else:
		resultados = request.POST
		js = mainCalendar.anadirSemanasExcluidas(resultados, request.session['json'])
		request.session['json'] = js
		
		return HttpResponseRedirect("/editarcalendario")

def intercambio_dias(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/editarcalendario')
	else:
		resultados = request.POST
		js = mainCalendar.anadirDiasIntercambio(resultados, request.session['json'])
		request.session['json'] = js
		
		return HttpResponseRedirect("/editarcalendario")