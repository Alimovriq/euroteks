from django.urls import path
from . import views


app_name = 'main_pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('requisites/', views.requisites, name='requisites'),
    path('success/', views.success, name='success'),
    path('feedback/', views.feedback, name='feedback'),
    # path('feedback/', views.FeedbackView.as_view(), name='feedback'),
]
