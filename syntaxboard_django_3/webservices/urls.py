from django.urls import path
from . import views

urlpatterns = [
    path('random_number/', views.random_number, name='random_number'),
    path('even_odd/', views.even_odd, name='even_odd'),
    path('get_custom_header/', views.get_custom_header, name='get_custom_header'),
]

# http://127.0.0.1:8000/webservices/random_number/
# http://127.0.0.1:8000/webservices/even_odd/

# For GET send in Params > Key > N1 > "value"
# For POST send in Body > form-data > N1 > "value"
# For PUT send in Params > Key > N1 > "value"

# http://127.0.0.1:8000/webservices/get_custom_header/
# http://localhost:8000/webservices/get_custom_header/
