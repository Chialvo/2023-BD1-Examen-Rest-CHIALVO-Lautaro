from django.urls import path, include
from api.views import *

urlpatterns = [
    path('customers/', customers, name='getAllCustomers'),
    path('customers/<str:pk>/', id_customers, name='getCustomerById'),

    path('suppliers/', suppliers, name='getAllSuppliers'),
    path('suppliers/<str:pk>/', id_suppliers, name='getSupplierById'),
    
    path("category/", categories, name="getAllCategories"),
    path("category/<str:pk>", id_categories , name="getCategoryById"), 

    path("product/", products, name="getAllProducts"),
    path("product/<str:pk>", id_products , name="getProductById"), 

    path("order/", orders, name="getAllOrders"),
    path("order/<str:pk>/", id_orders, name="getOrderById"),

    path("orderdetail/", details, name="getAllOrderDetails"),
    path("orderdetail/<str:pk>/<str:pk2>/", id_details, name="getOrderDetailById"),

    path("employee/", employees, name="getAllEmployees"),
    path("employee/<str:pk>/", id_employees,name="getEmployeeById"),

    path("employeedetail/<str:lastname>/", employees_by_lastname, name="getAllEmployeeDetails"),
    
    path("filtro1/", filtrar_por_birthday, name="getFiltro1"),
]