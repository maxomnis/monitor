#!coding=utf-8

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Poll ,Choice

admin.site.register(Poll) #注册Poll，使其在admin后台可以管理
admin.site.register(Choice)