from accounts.serializers import UserSerializer, ReportSerializer, UserRegistrationSerializer, UserLoginSerializer
from rest_framework import viewsets, status
from accounts.models import User, Report
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.permissions import IsPostOrOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)



# class UserProfileView(RetrieveAPIView):

#     permission_classes = (IsAuthenticated,)
#     authentication_class = JSONWebTokenAuthentication

#     def get(self, request):
#         try:
#             user_profile = UserProfile.objects.get(user=request.user)
#             status_code = status.HTTP_200_OK
#             response = {
#                 'success': 'true',
#                 'status code': status_code,
#                 'message': 'User profile fetched successfully',
#                 'data': [{
#                     'first_name': user_profile.first_name,
#                     'last_name': user_profile.last_name,
#                     'rut': user_profile.rut,
#                     'birth_date': user_profile.birth_date,
#                     }]
#                 }

#         except Exception as e:
#             status_code = status.HTTP_400_BAD_REQUEST
#             response = {
#                 'success': 'false',
#                 'status code': status.HTTP_400_BAD_REQUEST,
#                 'message': 'User does not exist',
#                 'error': str(e)
#                 }
#         return Response(response, status=status_code)