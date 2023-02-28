from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("ola, aluno!")

def wName(request, name):
    return HttpResponse(f"hello, {name}")