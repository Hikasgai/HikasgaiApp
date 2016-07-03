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
		resultados = request.POST
		print resultados

		calendarFile = mainCalendar.createCalendarJson(resultados)
        return HttpResponse(calendarFile)
