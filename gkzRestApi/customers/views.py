from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONparser
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializer


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data,safe=False)
        # In order to serialize objects, we ust set 'safe=false'
        
    elif request.method == 'POST':
        customer_data = JSONparser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(customer_serializer.errors, status=HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        Customer.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
    
@csrf_exempt
def customer_detail(request):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        customer_serializer = CustomerSerializer(customer)
        return JsonResponse(customer_serializer.data)
    
    elif request.method == 'PUT':
        customer_data = JSONparser().parse(request)
        customer_serializer = CustomerSerializer(customer, data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(CustomerSerializer.data)
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.methos == 'DELETE':
        customer.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    

@csrf_exempt
def customer_list_age(request, age):
    customers = Customer.object.filter(age=age)
    
    if request.method == 'GET':
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
            
        
    