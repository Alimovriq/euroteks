from django.contrib import admin
from django.urls import path, include


handler404 = 'core.views.page_not_found'

urlpatterns = [
    path('', include('main_pages.urls')),
    path('admin/', admin.site.urls),
]
