from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main_pages.urls')),
    path('admin/', admin.site.urls),
]
