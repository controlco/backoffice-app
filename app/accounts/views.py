from accounts.serializers import UserSerializer, ReportSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework import viewsets, status
from accounts.models import User, Report
from rest_framework import permissions, serializers
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from accounts.permissions import IsMyOrReadOnly, IsOwner
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from property_manager.serializers import PropertySerializer
from fcm_django.models import FCMDevice

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (IsMyOrReadOnly, )

    @action(methods=["GET"], detail=True)
    def reports_done(self, request, pk=None):
        user = self.get_object()
        reports_made = user.from_report.all()
        return Response([ReportSerializer(report).data for report in reports_made])

    @action(methods=["GET"], detail=True)
    def properties(self, request, pk=None):
        user = self.get_object()
        properties = user.property.all()
        return Response([PropertySerializer(property).data for property in properties])

    @action(methods=["POST", "DELETE"], detail=True)
    def device(self, request, pk=None):
        user = self.get_object()
        if request.method == "DELETE":
            current_device = FCMDevice.objects.filter(user=user).first()
            if current_device:
                current_device.delete()
            return Response({"status": "deleted"})
        elif all(field in request.data for field in ["token", "type"]):
            device_type = request.data["type"]
            current_device = FCMDevice.objects.filter(user=user).first()
            if current_device:
                current_device.registration_id = request.data["token"]
                current_device.type = device_type
                current_device.save()
                return Response({"status": "success"})
            FCMDevice.objects.create(
                registration_id=request.data["token"],
                user=user,
                type=device_type,
            )
            return Response({"status": "success"})
        return Response(
            {"Invalid Request": "Invalid Data"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
