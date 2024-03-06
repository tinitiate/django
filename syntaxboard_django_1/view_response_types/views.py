from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse
# import csv
import requests
from PIL import Image
from io import BytesIO

# Plain Text Response
# ###################################################################################
def http_response_plain_text(request):
    return HttpResponse("Plain Text Response", content_type="text/plain")

# XML Response
# ###################################################################################
def http_response_xml_text(request):
    response = """<?xml version="1.0" encoding="UTF-8"?>
                  <data>
                      <topic>Python Django</topic>
                      <heading>Response Types</heading>
                  </data>"""

    return HttpResponse(response, content_type="text/xml")


# HTTP Response
# ###################################################################################
def http_response_html(request):

    html_text = """<h1>HTML Response </h1>
                <p style="background-color:red; color:white;">HTML Response Output</p>"""

    return HttpResponse(html_text)


# JSON Response
# ###################################################################################
def json_response(request):
    return JsonResponse({'data':'tinitiate'})


# File Response
# ###################################################################################
def file_response(request):
    Imgfile = 'E:/code/PYTHON_TRAINING/Python_DJANGO/syntaxboard_django_1/view_response_types/image.png'
    with open(Imgfile, "rb") as f:
        return HttpResponse(f.read(), content_type="image/jpeg")


######################################################################
## STREAMING EXAMPLE 
## This will download a file with 1 to 100 each number on a new line
######################################################################
def generator():
    for x in range(1000):
        yield str(x) + "\n"

def streaming_http_response(queryset):
    response = StreamingHttpResponse( streaming_content=generator(),content_type='text/plain')

    response['Content-Disposition'] = 'attachment;filename=syntaxboard.txt'
    return response
