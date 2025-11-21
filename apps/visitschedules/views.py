from django.shortcuts import render
from rest_framework import viewsets
from .models import VisitSchedule
from .serializer import VisitScheduleSerializer

# Create your views here.
class VisitScheduleViewSet(viewsets.ModelViewSet):
    queryset = VisitSchedule.objects.all().order_by('scheduled_datetime')
    serializer_class = VisitScheduleSerializer
