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
def disenar_calendario(request):
	if request.method == 'GET':
		course_form = courseForm1()
		return render(request, 'asignaturas/disenar_calendario.html', {'course_form' : course_form})
	else:
		resultados = request.POST
		calendarFile = mainCalendar.createCalendarJson(resultados)
        request.session['json'] = json.loads(calendarFile)

        course_form2 = courseForm2()
        course_form3 = courseForm3()
        course_form4 = courseForm4()

        curso = request.session['json']['cursoAcademico']
        fic1 = request.session['json']['inicioCuatrimestreUno']
        fic2 = request.session['json']['inicioCuatrimestreDos']
        ffc1 = request.session['json']['finCuatrimestreUno']
        ffc2 = request.session['json']['finCuatrimestreDos']

        return render(request, 'asignaturas/mostrar_calendario.html', {'curso' : curso, 'fic1': fic1, 'ffc1': ffc1, 'fic2':fic2, 'ffc2':ffc2, 'course_form2' : course_form2, 'course_form3' : course_form3, 'course_form4' : course_form4})
