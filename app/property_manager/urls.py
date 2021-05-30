from django.urls import path, include
from property_manager import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('properties', views.PropertyViewSet)
router.register('regions', views.RegionViewSet)
router.register('districts', views.DistrictViewSet)
router.register('images', views.ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
