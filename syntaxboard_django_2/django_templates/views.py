# File: views.py of the New App "app_django_html_templates"
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Python Template
def simple_template_python(request):

    # Create Template Object
    template = loader.get_template('django_template_basics.html')

    # Data (context) to be passed to template
    context = {
        'course_list': ['basic','advanced','web development','Interview QnA'],
        'l_title': 'Welcome to Python Training',
        'course_name':'PYTHON',
    }
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END

    
# Java Template
def simple_template_java(request):

    # Create Template Object
    template = loader.get_template('django_template_basics.html')


    # Data (context) to be passed to template
    context = {
        'course_list': ['core','advanced','spring'],
        'l_title': 'Welcome to Java Training',
        'course_name':'JAVA',
    }
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END


# DB Template
def simple_template_db(request):

    # Create Template Object
    template = loader.get_template('django_template_basics.html')


    # Data (context) to be passed to template
    context = {
        'course_list': ['SQL','TSQL','ADMIN'],
        'l_title': 'Welcome DB Training',
        'course_name':'DB',
    }
    
    # Use the "context" to render the HTML Template to display values
    return HttpResponse(template.render(context, request))
# END




# Template Inheritance Callers
# results=[[1, 2, 3, 4,], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# https://stackoverflow.com/questions/9388064/django-template-turn-array-into-html-table


def caller_borders(request):
    
    
    multi_line_data = {"data": zip( ["Python Scripts","Python OOP","Python Libraries"]
                                   ,[ "Training for Python as Scripting Language"
                                     ,"Training for Python Object Oriented programming"
                                     ,"Training for Python Libraries for real world usage"])}
    print(multi_line_data)

    # Create Template Object
    template = loader.get_template('inheritance_caller_borders.html')
    context = multi_line_data
    
    return HttpResponse(template.render(context, request))
# END


def caller_table(request):
    list_of_lists_data = {"data": [ ["Python Scripts","Training for Python as Scripting Language"]
                                   ,["Python OOP","Training for Python Object Oriented programming"]
                                   ,["Python Libraries","Training for Python Libraries for real world usage"]]}

    # Create Template Object
    template = loader.get_template('inheritance_caller_table.html')
    context = list_of_lists_data
    
    return HttpResponse(template.render(context, request))
# END


