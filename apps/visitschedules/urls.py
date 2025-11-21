from django.urls import path, include
from rest_framework import routers
from .views import VisitScheduleViewSet

app_name = 'visitschedules'

router = routers.DefaultRouter()
router.register('', VisitScheduleViewSet, basename='agendamento-de-visita')

urlpatterns = [
    path('', include(router.urls)),
]