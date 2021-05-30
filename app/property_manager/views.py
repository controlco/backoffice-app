from property_manager.serializers import PropertySerializer, RegionSerializer, DistrictSerializer, ImageSerializer
from rest_framework import viewsets
from property_manager.models import Property, Region, District, Image
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from property_manager.permissions import IsOwnerOrReadOnly, IsPropertyOwnerOrReadOnly
from rest_framework.permissions import AllowAny
# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    # @action(methods=["POST"], detail=True, permission_classes=[IsPropertyOwnerOrReadOnly])
    # def images(self, request, pk=None):
    #     property = self.get_object()
    #     title = self.request.data["title"]
    #     cover = self.request.data["cover"]
    #     image = Image.objects.create(title=title, cover=cover, property=property)
    #     return Response(ImageSerializer(image).data)

    

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    #permission_classes = (IsPropertyOwnerOrReadOnly, )
    permission_classes = (AllowAny, )


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
