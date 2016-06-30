from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AlumnoForm, UserForm, ProfesorForm
from django.contrib.auth.decorators import login_required

def index(request):
    #suma = 2 + 2
    return render(request, 'index.html')

#Aqui se os va a petar el culo al hacer las pruebas
def registro(request):
    registrado = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #Si los dos formularios son correctos
        if user_form.is_valid():
        #and
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            if request.POST.get('tipo') == 'profesor':
                profesor_form = ProfesorForm(data=request.POST)
                if profesor_form.is_valid():
                    profesor = profesor_form.save(commit=False)
                    profesor.usuario = user
                    profesor.save()
                else:
                    messages.error(request, 'Hay campos incorrectos')
                    return HttpResponseRedirect('/signup')
            elif request.POST.get('tipo') == 'alumno':
                alumno_form = AlumnoForm(data=request.POST)
                if alumno_form.is_valid():
                    alumno = profesor_form.save(commit=False)
                    alumno.usuario = user
                    alumno.save()
                else:
                    messages.error(request, 'Hay campos incorrectos')
                    return HttpResponseRedirect('/signup')
            user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password'])
            login(request, user)
            registrado = True
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Hay campos incorrectos')
            return HttpResponseRedirect('/signup')
    #se crea el formulario para que el usuario pueda registrarse
    else:
        user_form = UserForm()
        profesor_form = ProfesorForm()
        alumno_form = AlumnoForm()
        context = {
            'user_form' : user_form,
            'profesor_form': profesor_form,
            'alumno_form': alumno_form,
            'registrado': registrado
        }
        return render(request, 'usuarios/registro.html', context)

#Iniciar sesion
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Comprobar si existe el usuario en la bd
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'El usuario que intentas introducir no existe o la contrasenia no es correcta')
            return HttpResponseRedirect('/login')
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        return render(request, 'usuarios/login.html', {})

#Cerrar sesion
@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_profile(request):
    return render(request, 'usuarios/perfil.html')