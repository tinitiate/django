from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500

urlpatterns = [
    # path('', include('homepage.urls')),
    path('single_view/', include('single_view.urls')),
    path('multiple_views/', include('multiple_views.urls')),
    path('view_response_types/', include('view_response_types.urls')),
    path('admin/', admin.site.urls),
]


# page not found 404
# localhost:8000/single_view/some_page_that_doest_exist
# ###############################################################################
# path('404/', views.page_not_found_404),
handler404 = 'single_view.views.handler404'