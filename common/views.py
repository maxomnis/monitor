#!coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
import  json

def index(request):
    context=''
    return render(request, 'common/index.html', context)

def login(request):
    response_data={'name':'jack', 'age':10}
    HttpResponse(json.dumps(response_data), content_type="application/json")

