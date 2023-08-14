from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_request, name='submit_request'),
    path('tracking/', views.request_tracking, name='request_tracking'),
]
