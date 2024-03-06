from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('django_forms/', include('django_forms.urls')),
    path('django_templates/', include('django_templates.urls')),
    path('django_cookies/', include('django_cookies.urls')),
    path('django_sessions/', include('django_sessions.urls')),
    path('admin/', admin.site.urls),
]
