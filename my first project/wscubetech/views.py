from django.http import HttpResponse, request
from django.shortcuts import render

# ------------------------------------

def home(request):
    

    datas={'title':'Home Page'}
    return render(request,'templates\index.html',datas)
    

def contact(request):
    datas={'title':'Contact Page'}
    return render(request,'contact.html',datas)

def service(request):
    datas={'title':'service Page'}
    return render(request,'service.html',datas)

def team(request):
    datas={'title':'team Page'}
    return render(request,'team.html',datas)

def blog(request):
    datas={'title':'blog Page'}
    return render(request,'blog.html',datas)

