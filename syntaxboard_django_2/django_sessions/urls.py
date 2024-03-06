from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('secured_page/', views.secured_page, name='secured_page'),
    path('logout/', views.logout, name='logout'),
]

# localhost:8000/django_sessions/login/
# localhost:8000/django_sessions/secured_page/
# localhost:8000/django_sessions/logout/