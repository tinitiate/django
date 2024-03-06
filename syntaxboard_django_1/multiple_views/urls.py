from django.urls import include, path
# Get the views from the view folder
from .views import greetings
from .views import calc

urlpatterns = [
    # localhost:8000/multiple_views/hello/tinitiate
    # localhost:8000/multiple_views/bday/tinitiate
    path('hello/<str:in_data>', greetings.hello, name='hello'),
    path('bday/<str:in_data>', greetings.bday, name='bday'),

    # localhost:8000/multiple_views/num_square/3
    # localhost:8000/multiple_views/even_or_odd/1
    path('num_square/<int:in_number>', calc.num_square, name='num_square'),
    path('even_or_odd/<int:in_number>', calc.even_or_odd, name='even_or_odd'),
]
