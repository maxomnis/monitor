#!coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import  json

def index(request):
    context=''
    return render(request, 'common/index.html', context)

def success(request):
    context=''
    return render(request, 'common/success.html', context)

#@require_http_methods(["GET", "POST"])   #装饰器

def login(request):
   # print str(response_data)
   # return HttpResponse(json.dumps(response_data), content_type="application/json")
    #question_id='hello'
    #return HttpResponse("You're voting on question %s." % question_id)
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')
        #isajax=request.is_ajax()
        #return HttpResponse(isajax)
        #return redirect('http://www.baidu.com/')
        #return HttpResponse(account+"...."+password)
        #return render(request,'common/success.html','')
        #return HttpResponseRedirect('/success/')
        result={"status":0, "data":"", "msg":"登录失败"}
        if(account=="jack" and password=="jack"):
            result['status']=1
            result['msg']='index/success/'
        return HttpResponse(json.dumps(result), content_type="application/json")

    else:
        pass



