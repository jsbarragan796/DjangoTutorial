# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Imagen
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
admin.site.register(Imagen)
admin.site.register(User, UserAdmin)