from django.urls import path, include
from rest_framework import routers
from .views import VisitorViewSet
from . import views

app_name = 'visitors'

router = routers.DefaultRouter()
router.register('visitors', VisitorViewSet, basename='visitantes')

urlpatterns = [
    path('', include(router.urls)),
]