from django.urls import path, include
from rest_framework import routers
from .views import BuildingViewSet

app_name = 'buildings'

router = routers.DefaultRouter()
router.register('', BuildingViewSet, basename='prédios')

urlpatterns = [
    path('', include(router.urls)),
]