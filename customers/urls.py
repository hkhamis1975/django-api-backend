from django.urls import path
# from rest_framework import routers
from customers import views
from .views import customers

app_name = 'customers'

urlpatterns = [
    path('api/customers/', views.customers, name='customers'),
    path('api/customers/<int:id>/', views.customers, name='customer'),
]
