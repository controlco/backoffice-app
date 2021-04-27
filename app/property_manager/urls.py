from django.urls import path, include
from property_manager import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('properties', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
