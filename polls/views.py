from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse ("Hello World, This is first Page of Polls App :D")