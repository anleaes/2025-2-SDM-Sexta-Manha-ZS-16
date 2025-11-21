from django.shortcuts import render
from rest_framework import viewsets
from .models import Visitor
from .serializers import VisitorSerializer

# Create your views here.
class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all().order_by('id')
    serializer_class = VisitorSerializer