from django.shortcuts import render, redirect
from X.forms import FormAnimal, FormPersona
from X.models import Animales, Persona
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import MyUserCreationForm
from .forms import MyLoginForm
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, 'Xapp/index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Vista de login
def login_view(request):
    if request.method == 'POST':
        form = MyLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página principal
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = MyLoginForm()
    
    return render(request, 'Xapp/login.html', {'form': form})
# Vista de registro de usuario
def register_view(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = MyUserCreationForm()

    return render(request, 'Xapp/register.html', {'form': form})

# Vista de listado de animales
def listadoAnimales(request):
    animaless = Animales.objects.all()
    data = {'animaless': animaless}
    return render(request, 'Xapp/animales.html', data)

# Vista de listado de personas
def listadoPersonas(request):
    personas = Persona.objects.all()
    data = {'personas': personas}
    return render(request, 'Xapp/personas.html', data)

# Vista de agregar un animal
def agregarAnimales(request):
    form = FormAnimal()  # Cambié FormBasque a FormAnimal
    if request.method == 'POST':
        form = FormAnimal(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal agregado exitosamente.')  # Mensaje de éxito
        else:
            messages.error(request, 'Errores al agregar el animal.')  # Mensaje de error
        return redirect('listadoAnimales')  # Redirige a la lista de animales
    data = {'form': form, 'p1' : 1}
    return render(request, 'Xapp/agregarAnimal.html', data)

# Vista de agregar una persona
def agregarPersonas(request):
    form = FormPersona()  
    if request.method == 'POST':
        form = FormPersona(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona agregada exitosamente.')  
        else:
            messages.error(request, 'Errores al agregar la persona.')  
        return redirect('listadoPersonas')  
    data = {'form': form, 'p2' : 2}
    return render(request, 'Xapp/agregarPersona.html', data)

# Vista de actualizar un animal
def actualizarAnimales(request, id):
    animales = Animales.objects.get(id=id)
    form = FormAnimal(instance=animales)  # Cambié FormBasque a FormAnimal
    if request.method == 'POST':
        form = FormAnimal(request.POST, request.FILES, instance=animales)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal actualizado exitosamente.')  # Mensaje de éxito
        else:
            messages.error(request, 'Errores al actualizar el animal.')  # Mensaje de error
        return redirect('listadoAnimales')  # Redirige a la lista de animales
    data = {'form': form}
    return render(request, 'Xapp/agregarAnimal.html', data)

# Vista de actualizar una persona
def actualizarPersona(request, id):
    persona = Persona.objects.get(id=id)
    form = FormPersona(instance=persona)  # Cambié FormManages a FormPersona
    if request.method == 'POST':
        form = FormPersona(request.POST, instance=persona)
        if form.is_valid():
            form.save()
            messages.success(request, 'Persona actualizada exitosamente.')  # Mensaje de éxito
        else:
            messages.error(request, 'Errores al actualizar la persona.')  # Mensaje de error
        return redirect('listadoPersonas')  # Redirige a la lista de personas
    data = {'form': form}
    return render(request, 'Xapp/agregarPersona.html', data)

# Vista de eliminar un animal
def eliminarAnimales(request, id):
    animales = Animales.objects.get(id=id)
    animales.delete()
    messages.success(request, 'Animal eliminado exitosamente.')  # Mensaje de éxito
    return redirect('listadoAnimales')  # Redirige a la lista de animales

# Vista de eliminar una persona
def eliminarPersona(request, id):
    persona = Persona.objects.get(id=id)
    persona.delete()
    messages.success(request, 'Persona eliminada exitosamente.')  # Mensaje de éxito
    return redirect('listadoPersonas')  # Redirige a la lista de personas
