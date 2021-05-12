from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('reports', views.ReportViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
