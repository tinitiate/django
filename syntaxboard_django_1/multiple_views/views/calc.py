from django.shortcuts import render
from django.http import HttpResponse

def num_square(request, in_number):

    response = "Square of " + str(in_number) + " is: " + str(pow(in_number,2))
    return HttpResponse(response)


def even_or_odd(request, in_number):

    s_data = str(in_number)
    if (in_number%2) == 0:
        response = s_data + " is a even number"
    else:
        response = s_data + " is a odd number"

    return HttpResponse(response)