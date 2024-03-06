from django.urls import path
from . import views

urlpatterns = [
    path('cookie_set/', views.cookie_set, name='cookie_set'),
    path('cookie_view/', views.cookie_view, name='cookie_view'),
    path('cookie_delete/', views.cookie_delete, name='cookie_delete'),
]


#  localhost:8000/django_cookies/cookie_set/
#  localhost:8000/django_cookies/cookie_view/
#  localhost:8000/django_cookies/cookie_delete/
