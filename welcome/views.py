from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello my Test Page")
# Create your views here.
