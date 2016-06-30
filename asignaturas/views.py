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
from .forms import courseForm

def user_courses(request):
	return render(request, 'asignaturas/courses.html')

#def course_detail(request):
#	return render(request, 'asignaturas/course_detail.html')

@csrf_exempt	
def disenar_calendario(request):
	if request.method == 'GET':
		course_form = courseForm()
		return render(request, 'asignaturas/disenar_calendario.html', {'course_form' : course_form})
	else:
		body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)

        data = {}
        asignaturas = []
        for asig in received_json_data["asignaturas"]:
            asignaturas.append(mainData.getHorarioAsignatura(asig))
        data["asignaturas"] = asignaturas
        calendarFile = mainCalendar.createCalendar(data, mainData.getDiasSemanas())

        #Se convierte a JSON para poder gestionarlo bien en el cliente
        calendario = {}
        calendario["calendario"] = calendarFile
        return HttpResponse(json.dumps(calendario))


@csrf_exempt
def course_detail(request):
    if request.method == 'GET': #Si se hace un GET se muestra solamente la vista
        return render(request, 'asignaturas/course_detail.html', {})
    else: #Si es un post se crea el calendario y se envia un JSON con el fichero
        body_unicode = request.body.decode('utf-8')
        received_json_data = json.loads(body_unicode)

        data = {}
        asignaturas = []
        for asig in received_json_data["asignaturas"]:
            asignaturas.append(mainData.getHorarioAsignatura(asig))
        data["asignaturas"] = asignaturas
        calendarFile = mainCalendar.createCalendar(data, mainData.getDiasSemanas())

        #Se convierte a JSON para poder gestionarlo bien en el cliente
        calendario = {}
        calendario["calendario"] = calendarFile
        return HttpResponse(json.dumps(calendario))