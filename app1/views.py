from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse("<h1>this is app1</h1>")
def second(request):
    return HttpResponse("<marquee>my second view</marquee>")
