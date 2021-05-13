from accounts.serializers import UserSerializer, ReportSerializer
from rest_framework import viewsets
from accounts.models import User, Report
from rest_framework import permissions
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
