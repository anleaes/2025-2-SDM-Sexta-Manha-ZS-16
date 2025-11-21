from rest_framework import serializers
from .models import VisitSchedule

class VisitScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitSchedule
        fields = '__all__'