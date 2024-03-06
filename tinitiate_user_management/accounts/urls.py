# backend/server/apps/accounts/urls.py file

from django.urls import include, re_path

urlpatterns = [
    re_path('', include('djoser.urls')),
    re_path('', include('djoser.urls.authtoken')),
]

# Register http://127.0.0.1:8000/accounts/users
# Login  http://127.0.0.1:8000/accounts/token/login
# Email: admin@admin.com SuperUser: admin, pass: Test!2345678
# http://127.0.0.1:8000/accounts/users/me/
# http://127.0.0.1:8000/accounts/token/logout/