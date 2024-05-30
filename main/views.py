from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("Hello World")

def home(response):
    return render(response, "main/home.html",{})