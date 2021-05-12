from property_manager.serializers import PropertySerializer, RegionSerializer, DistrictSerializer
from rest_framework import viewsets
from property_manager.models import Property, Region, District
from rest_framework import permissions
from property_manager.permissions import IsOwnerOrReadOnly

# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    # called when request POST
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
