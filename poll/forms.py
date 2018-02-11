
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm
from django.contrib.auth.forms import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import Imagen, User
from django.contrib.auth import password_validation


# Create your models here.


class ImageFrom(ModelForm):
    class Meta:
        model = Imagen
        fields = ['url', 'title', 'type', 'imageFile', 'description']


class UserForm(ModelForm):
    username = forms.CharField(label="Usuario", max_length=20)
    first_name = forms.CharField(label="Nombres",max_length=20)
    last_name = forms.CharField(label="Apellidos",max_length=20)
    email = forms.EmailField(label="Correo electronico")
    password = forms.CharField(label="Nueva Contraseña",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Nueva Contraseña",widget=forms.PasswordInput())
    foto = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name','foto', 'pais' , 'ciudad' , 'direccion','email', 'password', 'password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya ha sido tomado')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Correo ya ha sido registrado')
        return email

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2


class UserUpdateForm(ModelForm):
    pk_user = None
    first_name = forms.CharField(label="Nombres", max_length=20)
    last_name = forms.CharField(label="Apellidos", max_length=20)
    email = forms.EmailField(label="Correo electrónico")
    foto = forms.ImageField(required=False)
    pais = forms.CharField()
    ciudad = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=50)


    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'pais', 'ciudad', 'direccion', 'email', 'foto']


    def clean_email(self):
        email = self.cleaned_data['email']
        busqueda = User.objects.filter(email=email)
        if busqueda:
            user = busqueda.first()
            if user.pk != self.pk_user:
                raise forms.ValidationError('Correo ya ha sido registrado')
            else:
                return email
        return email


class UserChangePassword(PasswordChangeForm):

    old_password = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
    new_password1 = forms.CharField(label="Contraseña Nueva",widget=forms.PasswordInput())
    new_password2 = forms.CharField(label="Contraseña Nueva", widget=forms.PasswordInput())


    def clean_old_password(self):
        try:
            return super(UserChangePassword, self).clean_old_password()
        except:
            raise forms.ValidationError("Contraseña actual incorrecta")
    def clean_new_password2(self):
        password1 = self.cleaned_data['new_password1']
        password2 = self.cleaned_data['new_password2']
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Contraseñas no coinciden')
        try:
            password_validation.validate_password(password2, self.user)
        except password_validation.ValidationError as errores:
            mensajes = []
            for m in errores.messages:
                if m == 'This password is too short. It must contain at least 8 characters.':
                    mensajes.append('Contraseña muy corta, debe contener más de 7 caracteres')
                if m == 'This password is too common.':
                    mensajes.append('Contraseña muy común')
                if m == 'This password is entirely numeric.':
                    mensajes.append('Contraseña no puede contener solo números')
                if m.startswith("The password is too similar"):
                    mensajes.append('Contraseña muy similar a los datos del usuario')
            raise forms.ValidationError(mensajes)
        return password2
