from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render

def view_no_param(request):
    return HttpResponse("Welcome to SyntaxBoard Django Test Home Page Version 1.0")

def view_integer_param(request, in_data):
    response = "Integer Data Provided: " + str(in_data)
    return HttpResponse(response)

def view_string_param(request, in_data):
    response = "String Data Provided: " + in_data
    return HttpResponse(response)

def even_or_odd(request, in_number):
    
    s_data = str(in_number)

    if (in_number%2) == 0:
        response = s_data + " is a even number"
    else:
        response = s_data + " is a odd number"

    return HttpResponse(response)


def addnums(request, in_number,in_string):
    response = "int_input: " + str(in_number)
    response = response + ", string_input: " + in_string
    return HttpResponse(response)


# matching Patterns
def view_numbers(request,data):
    return HttpResponse("Numbers: " + str(data))


def view_strings(request,data):
    return HttpResponse("Strings: " + data)


# Redirects
# Temporary vs. Permanent Redirect
# Temporary: Status 302 found. The found indicates a temporary redirect which means,
#            "Change Landing page for sale-days"
# Permanent: Status Code 301 represents Permanent Redirect.

def redirect_permanent(request):
    return HttpResponse("This is a message from views.redirect_permanent !!")

def redirect_301(request):
    return HttpResponsePermanentRedirect(reverse('redirect_permanent'))


def redirect_temporary(request):
    return HttpResponse("This is a temp landing message from views.redirect_temporary !!")

def redirect_302(request):
    return HttpResponseRedirect(reverse('redirect_temporary'))


# Page Not Found
def handler404(request, exception):
    #def page_not_found_404(request):
    return render(request,'html404.html')



