from property_manager.serializers import PropertySerializer, RegionSerializer, DistrictSerializer
from rest_framework import viewsets
from property_manager.models import Property, Region, District
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from property_manager.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = (IsOwnerOrReadOnly, )


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (AllowAny,)

    @action(methods=["GET"], detail=True)
    def districts(self, request, pk=None):
        region = self.get_object()
        districts = region.district.all()
        return Response([DistrictSerializer(district).data for district in districts])


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (AllowAny,)

    @action(methods=["GET"], detail=True)
    def properties(self, request, pk=None):
        district = self.get_object()
        properties = district.property.all()
        return Response([PropertySerializer(property).data for property in properties])
