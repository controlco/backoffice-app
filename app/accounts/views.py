from accounts.serializers import UserSerializer, ReportSerializer, UserRegistrationSerializer
from rest_framework import viewsets, status
from accounts.models import User, Report, UserProfile
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from accounts.permissions import IsPostOrOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsPostOrOwnerOrReadOnly, )

    @action(methods=["GET"], detail=True)
    def reports_done(self, request, pk=None):
        user = self.get_object()
        reports_made = user.from_report.all()
        return Response([ReportSerializer(report).data for report in reports_made])


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class UserRegistrationView(CreateAPIView):
    
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)