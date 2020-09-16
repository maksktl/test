from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import json

def index(request):
    return HttpResponse("Hello World")