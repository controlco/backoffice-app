from property_manager.serializers import PropertySerializer, RegionSerializer, DistrictSerializer, ImageSerializer, MeetingSerializer
from rest_framework import viewsets
from property_manager.models import Property, Region, District, Image, Meeting
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from property_manager.permissions import IsOwnerOrReadOnly, IsPropertyOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist, ValidationError

# Create your views here.


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(methods=["GET", "POST", "DELETE"], detail=True)
    def meetings(self, request, pk=None):
        if request.method == 'GET':
            property = self.get_object()
            meetings = property.meeting.all()
            return Response([MeetingSerializer(m).data for m in meetings])
        elif request.method == 'POST':
            permission_classes = (IsOwnerOrReadOnly, )
            if all(field in request.data for field in ["date", "hour"]):
                try:
                    prev_meeting = Meeting.objects.get(
                        date=request.data["date"], hour=request.data["hour"])
                    return Response({"Invalid Request": "duplicate key value violates unique constraint", 'DETAIL': 'Key (date, hour)'},
                                    status=status.HTTP_400_BAD_REQUEST)
                except ObjectDoesNotExist as err:
                    try:
                        meeting = Meeting(visitor=request.user, hour=request.data["hour"],
                                          property=self.get_object(), date=request.data["date"])
                        meeting.full_clean()
                        meeting.save()
                        meeting_serializer = MeetingSerializer(meeting)
                        return Response(meeting_serializer.data)
                    except ValidationError as err:
                        return Response({"Invalid Request": "Invalid value for hour", },
                                        status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(
                    {"Invalid Request": "Date is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            if all(field in request.data for field in ["id"]):
                meeting = Meeting.objects.get(
                    id=request.data["id"])
                meeting.delete()
                return Response({'Success': 'Meeting deleted'},
                                status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {"Invalid Request": "id is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # permission_classes = (IsPropertyOwnerOrReadOnly, )
    permission_classes = (AllowAny, )


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = (AllowAny,)

    @ action(methods=["GET"], detail=True)
    def districts(self, request, pk=None):
        region = self.get_object()
        districts = region.district.all()
        return Response([DistrictSerializer(district).data for district in districts])


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = (AllowAny,)

    @ action(methods=["GET"], detail=True)
    def properties(self, request, pk=None):
        district = self.get_object()
        properties = district.property.all()
        return Response([PropertySerializer(property).data for property in properties])


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = PropertySerializer

    # permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(visitor=self.request.user)
