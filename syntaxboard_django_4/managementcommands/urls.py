from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('limited_offer/', views.limited_offer, name='limited_offer'),
]


# At commandline start the project, using the command:

# python manage.py runserver

# Run a test to see the APP working
# Login using the URL:  http://localhost:8000/managementcommands/test
# Execute the Custom Management Commands at the command line in a seperate window

# python manage.py current_time

# Offers page  http://localhost:8000/managementcommands/limited_offer 
# will show offers present
# Execute the Custom Management Commands to disable the offer at the commandline.

# python manage.py offer_control -disable

# Offers page http://localhost:8000/managementcommands/limited_offer
# will show offers not available
# Enable the offers by running the following at the commandline

# python manage.py offer_control -enable

# Offers page http://localhost:8000/managementcommands/limited_offer
#  will again show offers.
