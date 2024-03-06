from django.shortcuts import render
from django.http import HttpResponse

def hello(request, in_data):
    response = "Hello: " + str(in_data)
    return HttpResponse(response)

def bday(request, in_data):
    response = "Happy Birthday: " + str(in_data)
    return HttpResponse(response)

