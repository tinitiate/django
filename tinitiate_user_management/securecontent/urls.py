# backend/server/apps/accounts/urls.py file
# from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    path('securedata', views.securedata),
]

# Check is Auth or Not http://127.0.0.1:8000/securecontent/securedata
# HTTP METHOD: GET
# Body:
# {"username": "admin"} 
# Header: 
# {"Authorization":"Token YOUR_TOKEN_HERE"}
