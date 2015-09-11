from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def serverinfo(request):
    return render(request, 'server/serverinfo.html', '')
