from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import customer
from .serializers import customerSerializer

def demo(req):
    return HttpResponse("from api")


# List all books / Create a book
class customerListCreateView(generics.ListCreateAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer
    
class customerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = customer.objects.all()
    serializer_class = customerSerializer