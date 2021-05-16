from django.urls import path, include
from accounts import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

router = DefaultRouter()
router.register('reports', views.ReportViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^signup', views.UserRegistrationView.as_view()),
    url(r'^login', views.UserLoginView.as_view()),

]
