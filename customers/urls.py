from django.urls import path
# from rest_framework import routers
from customers import views
from .views import customers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'customers'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/customers/', views.customers, name='customers'),
    path('api/customers/<int:id>/', views.customer, name='customer'),
]
