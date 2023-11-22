from django.urls import path, include
from api.views import *

urlpatterns = [
    path('customers/', customers, name='getAllCustomers'),
    path('customers/<str:pk>/', id_customers, name='getCustomerById'),
]