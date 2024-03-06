from .forms import LoginForm
from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create the Session KEY "userid" and assign value from the USERID TEXT BOX
def login(request):

    if request.method == 'POST':
        # Create a New Global Response Object
        response = HttpResponse('test')

        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():

            # Set the USERID as session varaible
            request.session['userid'] = loginForm.cleaned_data['userid']

            return redirect('/django_sessions/secured_page/')

    else:
        form = LoginForm()
        return render(request,'session_login.html',{'form':form})


# This page will be shown only if there is a login
def secured_page(request):

    template = loader.get_template('session_secured_page.html')
    
    # Check if the Session KEY "userid" exists
    # if request.session.has_key('userid'):
    if request.session.get('userid')=='abc':
        # Check if the Session KEY "userid" has a value assigned
        if request.session['userid']:
        # Data (context) to be passed to template
            context = {
                'l_user': request.session['userid']
            }
        else:
            context = { }
    else:
        context = { }

    return HttpResponse(template.render(context, request))


# This will clear the SESSION KEY "userid"
def logout(request):

    if request.session['userid']:
        l_user = request.session['userid']

    del request.session['userid']

    return HttpResponse("Successfully %s Logged out !"%l_user)
    
    