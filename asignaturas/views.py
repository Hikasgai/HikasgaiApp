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
import SOAPpy
# El siguiente metodo especifica lo que debe suceder cuando
# todos los formularios han sido subidos y comprobados

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
        courseform=course_form(data=request.POST)
        if courseform.is_valid():
            resultados = request.POST
            calendarFile = mainCalendar.createCalendarJson(resultados)
            request.session['json'] = json.loads(calendarFile)
            return HttpResponseRedirect("/editarcalendario")
        else: 
            print courseform.errors
            return HttpResponseRedirect("/crearcalendario")

        

@csrf_exempt
def editar_calendario(request):

    curso = request.session['json']['calendario']['cursoAcademico']
    fic1 = request.session['json']['calendario']['inicioCuatrimestreUno']
    fic2 = request.session['json']['calendario']['inicioCuatrimestreDos']
    ffc1 = request.session['json']['calendario']['finCuatrimestreUno']
    ffc2 = request.session['json']['calendario']['finCuatrimestreDos']
    dnl = request.session['json']['calendario']['diasSemanalesNoLectivos']
    dsc = request.session['json']['calendario']['diasSinClase']
    phe = request.session['json']['calendario']['periodosHorarioEspecial']
    se = request.session['json']['calendario']['semanasExcluidas']
    intd = request.session['json']['calendario']['intercambioDias']

    server = SOAPpy.SOAPProxy("www.abj-ws-devborja.c9users.io:8082")
    server2 = SOAPpy.SOAPProxy("www.cliente-pruebas-sw-magnasis-devborja.c9users.io:8080")
    print json.dumps(request.session['json'])
    ical = server.crearCalendario(json.dumps(request.session['json']['calendario']))#Mandar el objeto de calendario, no el json completo
    val = server2.validateCalendarJson(json.dumps(request.session['json']))#Hay que mandarle todo el json
    print val

    return render(request, 'asignaturas/editar_calendario.html', {'ical':ical ,'intd':intd,'phe':phe, 'se':se,'dsc':dsc,'dnl':dnl, 'curso' : curso, 'fic1': fic1, 'ffc1': ffc1, 'fic2':fic2, 'ffc2':ffc2, 'diasNoLectivos_form':diasNoLectivos_form(), 'diasSinClase_form':diasSinClase_form(), 'semanaHorarioEspecial_form':semanaHorarioEspecial_form(), 'diasCambiados_form':diasCambiados_form(), 'semanasExcluidas_form':semanasExcluidas_form()})


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