from django.shortcuts import render

# Create your views here.
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework import generics

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
