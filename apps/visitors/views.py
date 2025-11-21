from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializer import CategorySerializer

# Create your views here.
class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all().order_by('id')
    serializer_class = VisitorSerializer