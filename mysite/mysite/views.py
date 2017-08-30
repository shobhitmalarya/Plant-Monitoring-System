from django.shortcuts import HttpResponse
from django.shortcuts import render



def home(request):

    return HttpResponse("<h1>This is the home page of the app.</h1>")

