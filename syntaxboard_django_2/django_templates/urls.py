from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000
    path('sb_python', views.simple_template_python),
    path('sb_java', views.simple_template_java),
    path('sb_db', views.simple_template_db),
    path('sb_caller_borders', views.caller_borders),
    path('sb_caller_table', views.caller_table),
]

# Testing
# ###################################################################################
# http://localhost:8000/django_templates/sb_python
# http://localhost:8000/django_templates/sb_java
# http://localhost:8000/django_templates/sb_db

# ###################################################################################
# http://localhost:8000/django_templates/sb_caller_borders
# http://localhost:8000/django_templates/sb_caller_table
