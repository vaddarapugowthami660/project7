from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def three(request):
    return HttpResponse("<h1>this is gowthami</h1>")
def four(request):
    return HttpResponse("<h2>this is view page</h2>")