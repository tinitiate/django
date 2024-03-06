from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [

    # Simple URL
    # localhost:8000/single_view/view_no_param
    # ###############################################################################
    path('view_no_param/', views.view_no_param, name='view_no_param'),

    # Patterns
    # localhost:8000/single_view/data/1234
    # localhost:8000/single_view/data/abcd
    # ###############################################################################
    re_path(r'^data/(?P<data>[0-9]{4})$', views.view_numbers),
    re_path(r'^data/(?P<data>[-\w]+)$', views.view_strings),

    # Passing Parameters to Views
    # localhost:8000/single_view/view_integer_param/1
    # localhost:8000/single_view/view_string_param/Hello
    # localhost:8000/single_view/even_or_odd/1
    # localhost:8000/single_view/multi_input/1/abc
    # ###############################################################################
    path('view_integer_param/<int:in_data>', views.view_integer_param),
    path('view_string_param/<str:in_data>', views.view_string_param),
    path('even_or_odd/<int:in_number>', views.even_or_odd),
    path('multi_input/<int:in_number>/<str:in_string>', views.multi_input),

    # Redirects
    # localhost:8000/single_view/redirect_301
    # localhost:8000/single_view/redirect_302
    # ###############################################################################
    path('redirect_permanent', views.redirect_permanent, name='redirect_permanent'),
    path('redirect_temporary', views.redirect_temporary, name='redirect_temporary'),
    path('redirect_301', views.redirect_301),
    path('redirect_302', views.redirect_302),

]




