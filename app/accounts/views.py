from accounts.serializers import UserSerializer
from rest_framework import viewsets
from accounts.models import User

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
