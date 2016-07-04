from django.shortcuts import render
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
from .forms import courseForm1, courseForm2, courseForm3, courseForm4


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
