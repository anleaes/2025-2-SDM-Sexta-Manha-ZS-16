from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Building
from .serializer import BuildingSerializer

# Create your views here.
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all().order_by('name')
    serializer_class = BuildingSerializer