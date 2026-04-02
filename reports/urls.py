from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_form, name='report'),
    path('pickup/', views.pickup_request, name='pickup_request'),
    path('status/', views.status, name='status'),
]
