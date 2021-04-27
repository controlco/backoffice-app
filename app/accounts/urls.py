from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
