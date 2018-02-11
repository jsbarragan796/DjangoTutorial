# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .models import Imagen
from .forms import ImageFrom, UserForm, UserUpdateForm, UserChangePassword

# Create your views here.
def index(request):
    if request.user.is_authenticated():
        lista_imagenes = Imagen.objects.filter(user=request.user)
    else:
        lista_imagenes = Imagen.objects.all()
    context = {'lista_imagenes': lista_imagenes}

    return render(request, 'poll/index.html', context)


def add_image(request):
    if request.method == 'POST':
        form = ImageFrom(request.POST, request.FILES)
        if form.is_valid():
            new_imagen = Imagen(url=request.POST['url'],
                                title=request.POST.get('description'),
                                type=request.POST.get('type'),
                                imageFile=request.FILES['imageFile'],
                                user=request.user);
            new_imagen.save()

            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = ImageFrom()
    return render(request, 'poll/image_form.html', {'form': form})

def update_image(request):
    if request.method == 'POST':
        form = ImageFrom(request.POST, request.FILES)
        if form.is_valid():
            new_imagen = Imagen(url=request.POST['url'],
                                title=request.POST.get('description'),
                                type=request.POST.get('type'),
                                imageFile=request.FILES['imageFile'],
                                user=request.user);
            new_imagen.save()

            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = ImageFrom()
    return render(request, 'poll/image_form.html', {'form': form})



def user_registration_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username, password=password)
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = UserForm()
    return render(request, 'poll/user_registration.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated():
        return redirect(reverse('images:index'))
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect(reverse('images:index'))
        else:
            mensaje = 'Nombre de usuario o clave no valido'

    return render(request,'poll/login.html',{'mensaje': mensaje})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('images:index'))


def perfil(request):
    if request.user.is_authenticated():

        return render(request, 'poll/user_detalle.html')
    else:
        return index(request)

def perfil_actualizar(request):
    user_model = User.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user_model)
        form.pk_user = request.user.pk
        if form.is_valid():
            cleaned_data = form.cleaned_data
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            email = cleaned_data.get('email')
            user_model.first_name = first_name
            user_model.last_name = last_name
            user_model.email = email
            user_model.save()

            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = UserUpdateForm(instance=user_model)
    return render(request, 'poll/user_editar.html', {'form': form})


def cambiar_contrasenia(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserChangePassword(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Su contraseña fue exitosamente cambiada!', extra_tags='alert alert-success')
                return redirect(reverse('images:index'))
        else:
            form = UserChangePassword(request.user)
        return render(request, 'poll/cambiar_contrasenia.html', {'form': form})
    else:
        return redirect(reverse('images:index'))