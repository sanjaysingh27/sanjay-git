from turtle import title
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # data = {
    #     "title":"Home page",
    #     "hdata":[1,2,3,4,5,6,7,8,9,10],
    #     "number":[],
    #     "st_detail":[
    #         {'name':'sanjay','phone':8279408396},
    #         {'name':'geeta','phone':9879408397}
    #     ]
    # }
    return render(request,"index.html")

def about(request):
    return HttpResponse("<b>this is my about</b>")

def contact(request):
    return HttpResponse("<b>this is my contact</b>")

def blog(request):
    return HttpResponse("this is blog page")

def blog_post(request,postid):
    return HttpResponse(postid)