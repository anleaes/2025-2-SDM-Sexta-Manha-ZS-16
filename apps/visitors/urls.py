from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'visitors'

router = routers.DefaultRouter()
router.register('', VisitorViewSet, basename='visitantes')

urlpatterns = [
    path('', include(router.urls)),
]