from django.shortcuts import render
from .models import Pizza_Rest, Customers, All
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import Pizza_RestSerializer, CustomersSerializer, AllSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

class Pizza_RestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Pizza_Rest to be viewed or edited.
    """
    queryset = Pizza_Rest.objects.all().order_by('status_customer')
    serializer_class = Pizza_RestSerializer
    # permission_classes = [permissions.IsAuthenticated]
    
@csrf_exempt
def pizza_list(request):
    """
    List all code PizzaRest, or create a new pizza.
    """
    if request.method == 'GET':
        pizza = Pizza_Rest.objects.all()
        serializer = Pizza_RestSerializer(pizza, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Pizza_RestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def pizza_detail(request):
    """
    Retrieve, update or delete a code pizza.
    """
    try:
        pizza = Pizza_Rest.objects.get()
    except Pizza_Rest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Pizza_RestSerializer(pizza)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Pizza_RestSerializer(pizza, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pizza.delete()
        return HttpResponse(status=204)

    
class AllViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Pizza_Rest to be viewed or edited.
    """
    queryset = All.objects.all().order_by()
    serializer_class = AllSerializer
    # permission_classes = [permissions.IsAuthenticated]

# @csrf_exempt
# def all_list(request):
#     """
#     List all code All, or create a new All.
#     """
#     if request.method == 'GET':
#         all = All.objects.all()
#         serializer = AllSerializer(all, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AllSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

    

class CustomersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customer to be viewed or edited.
    """
    queryset = Customers.objects.all().order_by('customer_id')
    serializer_class = CustomersSerializer
    # permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def customer_list(request):
    """
    List all code Customer, or create a new customer.
    """
    if request.method == 'GET':
        customer = Customers.objects.all()
        serializer = CustomersSerializer(customer, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customer_detail(request):
    """
    Retrieve, update or delete a code customer.
    """
    try:
        customer = Customers.objects.get()
    except Customers.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomersSerializer(pizza)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomersSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)











