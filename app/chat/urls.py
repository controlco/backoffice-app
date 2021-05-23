from django.urls import path, include
from chat import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register('', views.MessageViewSet, basename='Message')

urlpatterns = [
    path('users/<int:user_pk>/messages/', include(router.urls)),
]
