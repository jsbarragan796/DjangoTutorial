# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Imagen(models.Model):
    url = models.CharField(max_length=1000,blank=True, null=True)
    title = models.CharField(max_length=150,blank=True)
    description = models.CharField(max_length=1000, null=True)
    type = models.CharField(max_length=5,blank=True)
    imageFile = models.ImageField(upload_to='images',null=True)
    user = models.ForeignKey(User, null=True)


