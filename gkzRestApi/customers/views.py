from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONparser
from rest_framework import status

from .models import Customer
from .serializers import CustomerSerializers


@csrf_exempt
def customer_list(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        customers_serializer = Cust
