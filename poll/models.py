# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

    foto = models.ImageField(upload_to='images', null=True)
    pais = models.CharField(max_length=36, null=True, blank=True)
    ciudad = models.CharField(max_length=20, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=True, blank=True)





class Imagen(models.Model):
    url = models.CharField(max_length=1000,blank=True, null=True)
    title = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5,blank=True)
    imageFile = models.ImageField(upload_to='images',null=True)
    user = models.ForeignKey(User, null=True)


