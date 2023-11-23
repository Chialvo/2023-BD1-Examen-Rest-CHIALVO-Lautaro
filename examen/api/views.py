from api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from api.models import *
from django.db.models import Q
from datetime import datetime

@api_view(['GET', 'POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])

def id_customers(request, pk):
    try:
        customer = Customers.objects.get(pk=pk)
    except Customers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = Suppliers.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def id_suppliers(request, pk):
    try:
        supplier = Suppliers.objects.get(pk=pk)
    except Suppliers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":         
        categories = Categories.objects.all()
        categoriesSerializers = CategorieSerializer(categories, many=True)
        return Response(categoriesSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        categorieNuevo = CategorieSerializer(data = request.data)
        if categorieNuevo.is_valid():
            categorieNuevo.save()
            return Response(categorieNuevo.data, status=status.HTTP_200_OK)
        return Response(categorieNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def id_categories(request, pk):
    try:
        categorie = Categories.objects.get(categoryid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategorieSerializer(categorie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['categoryid'] = pk
    
        serializer = CategorieSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def products(request):
    if request.method == "GET":         
        products = Products.objects.all()
        productSerializers = ProductSerializer(products, many=True)
        return Response(productSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        productNuevo = ProductSerializer(data=request.data)
        if productNuevo.is_valid():
            productNuevo.save()
            return Response(productNuevo.data, status=status.HTTP_200_OK)
        return Response(productNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_products(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def orders(request):
    if request.method == "GET":         
        orders = Orders.objects.all()
        orderSerializers = OrderSerializer(orders, many=True)
        return Response(orderSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderNuevo = OrderSerializer(data=request.data)
        if orderNuevo.is_valid():
            orderNuevo.save()
            return Response(orderNuevo.data, status=status.HTTP_200_OK)
        return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_orders(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def details(request):
    if request.method == "GET":         
        order_details = Orderdetails.objects.all()
        orderDetailsSerializers = OrderdetailSerializer(order_details, many=True)
        return Response(orderDetailsSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderDetailNuevo = OrderdetailSerializer(data=request.data)
        if orderDetailNuevo.is_valid():
            orderDetailNuevo.save()
            return Response(orderDetailNuevo.data, status=status.HTTP_200_OK)
        return Response(orderDetailNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_details(request, pk, pk2):
    try:
        order_detail = Orderdetails.objects.get(orderid=pk, productid=pk2)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderdetailSerializer(order_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderdetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_detail.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def employees(request):
    if request.method == "GET":         
        employees = Employees.objects.all()
        employeeSerializers = EmployeeSerializer(employees, many=True)
        return Response(employeeSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        employeeNuevo = EmployeeSerializer(data=request.data)
        if employeeNuevo.is_valid():
            employeeNuevo.save()
            return Response(employeeNuevo.data, status=status.HTTP_200_OK)
        return Response(employeeNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def id_employees(request, pk):
    try:
        employee = Employees.objects.get(employeeid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['employee_id'] = pk
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(["GET"])
def employees_by_lastname(request, lastname):
    employees = Employees.objects.filter(lastname=lastname)
    employeeSerializers = EmployeeSerializer(employees, many=True)
    return Response(employeeSerializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def filtro1(request):
    products = Products.objects.filter(productname__startswith= 'C', categoryid__categoryname="Beverages")
    productSerializers = ProductSerializer(products, many=True)
    return Response(productSerializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def filtrar_por_birthday(request, birthday):
    employees = Employees.objects.filter(birthday=birthday)
    employeeSerializers = EmployeeSerializer(employees, many=True)
    return Response(employeeSerializers.data, status=status.HTTP_200_OK)

@api_view(["GET", 'UPDATE'])
def filtro3(request):

    employees = Employees.objects.filter(Q(country__icontains='a') | Q(country__icontains='e') | Q(country__icontains='i') | Q(country__icontains='o') | Q(country__icontains='u'), salary__gt=2800, birthdate__lt=datetime(1990, 1, 1))

    employees.update(salary=5555)

    employeeSerializers = EmployeeSerializer(employees, many=True)
    return Response(employeeSerializers.data, status=status.HTTP_200_OK)

@api_view(["GET", 'UPDATE'])
def filtro4(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate,
            "country" : e.country,
            "newCountry" : request.query_params.get("newCountry"),
        }
        if e.birthdate.year >= int(year):
            resultados.append(resultado)
            e.coutry = request.query_params.get("newCountry")
            e.save()
    serializados = Filtro4Serializer(resultados, many=True)
    return Response(serializados.data)

"""
@api_view(["GET"])
def filtro4(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstnameicontains = letra, birthdateyear__gte = year)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate,
            "country" : e.country,
            "newCountry" : request.query_params.get("newCountry"),
        }
        resultados.append(resultado)
        e.country = request.query_params.get("newCountry")
        e.save()

    serializados = Filtro4Serializer(resultados, many=True)
    return Response(serializados.data)
    """

#la suma de UnitsInStock más UnitsOnOrder sea menor que la cantidad provista y donde Discontinued sea distinto de ‘1’.

@api_view(["GET"])
def punto1(request):
    proveedor = request.query_params.get("suplier")
    category = request.query_params.get("categoryid")
    stockmin = request.query_params.get("stockmin")

    productosFiltrados = Products.objects.filter(supplierid = proveedor, categoryid = category)

    productosFinales = []
    for i in productosFiltrados:
        stockFuturo = i.suma()
        if stockFuturo <= int(stockmin): #& i.discontinued != 1, (el discontinued esta en text field en el models y no tengo tiempo de cambiarlo)
            productosFinales.append(i)

    resultados = []

    for e in productosFinales:
        resultado = {
            "productid" : e.productid,
            "productname" : e.productname,
            "supplierid" : e.supplierid,
            "categoryid" : e.categoryid,
            "stockmin" : (e.unitsinstock + e.unitsonorder),
        }
        resultados.append(resultado)

    serializados = Punto1Serializer(resultados, many=True)
    print(serializados)
    return Response(serializados.data)

@api_view(["POST"])
def punto2(request):

    proveedor = request.query_params.get("suplierid")
    category = request.query_params.get("categoryid")
    stock = request.query_params.get("stockrequerido")
    cliente = request.query_params.get("customerid")
    empleado = request.query_params.get("employeeid")
    correo = request.query_params.get("shipperid")

    orderNuevo = OrderSerializer(data=request.data)
    if orderNuevo.is_valid():
        orderNuevo.save()
        return Response(orderNuevo.data, status=status.HTTP_200_OK)
    return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)
