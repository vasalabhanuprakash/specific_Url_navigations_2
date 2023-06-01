from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def yash(request):
    return HttpResponse('<h1> The Rocking start Yash </h1>')