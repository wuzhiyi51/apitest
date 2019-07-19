from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
import json

# Create your views here.

def Login(request):
    if request.method=='POST':
        result = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        result['username']=username
        result['password']=password
        data=json.dumps(result)
        return HttpResponse(data, content_type='application/json;charset=utf-8')

    # if request.method=='GET':
    #     username=request.GET.get('username')
    #     mobile=request.GET.get('mobile')
    #     return HttpResponse(username + mobile)

    else:
        return render_to_response('login.html')