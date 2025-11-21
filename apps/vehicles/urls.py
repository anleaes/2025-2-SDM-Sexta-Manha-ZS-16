from django.urls import path, include
from rest_framework import routers
from .views import VehicleViewSet

app_name = 'vehicles'

router = routers.DefaultRouter()
router.register('', VehicleViewSet, basename='veículos')

urlpatterns = [
    path('', include(router.urls) )
]