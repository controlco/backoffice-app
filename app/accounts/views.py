from accounts.serializers import UserSerializer, ReportSerializer
from rest_framework import viewsets
from accounts.models import User, Report
from rest_framework import permissions
from accounts.permissions import IsPostOrOwnerOrReadOnly

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsPostOrOwnerOrReadOnly, )


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
