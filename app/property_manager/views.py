from property_manager.serializers import PropertySerializer, RegionSerializer, DistrictSerializer
from rest_framework import viewsets
from property_manager.models import Property, Region, District
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
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

    @action(methods=["GET"], detail=True)
    def districts(self, request, pk=None):
        region = self.get_object()
        districts = region.district.all()
        return Response([DistrictSerializer(district).data for district in districts])
