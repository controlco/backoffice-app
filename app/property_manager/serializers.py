from rest_framework import serializers
from accounts.models import User
from property_manager.models import Property, Region, District, Image, Meeting, Notification


class DistrictSerializer(serializers.ModelSerializer):
  #  property = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['name', 'region', "id"]


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['name', 'number']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'title', 'cover', 'property']


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    district_name = serializers.ReadOnlyField(source='district.name')
    property_images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ['id', 'title', 'owner_id', 'owner', 'surface', 'adress',
                  'price', 'description', 'latitude', 'longitude', 'district',
                  'district_name', 'electricity_service', 'water_service', 'property_images']


class MeetingSerializer(serializers.ModelSerializer):
    visitor_id = serializers.ReadOnlyField(source='visitor.id')

    class Meta:
        model = Meeting
        fields = ['id', 'property', 'date', 'hour', 'visitor_id']


class NotificationSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(
        source='owner.first_name')
    owner_last_name = serializers.ReadOnlyField(
        source='owner.last_name')
    receiver_name = serializers.ReadOnlyField(
        source='receiver.first_name')
    receiver_last_name = serializers.ReadOnlyField(
        source='receiver.last_name')

    class Meta:
        model = Notification
        fields = ['title', 'content',
                  'owner_name', 'owner_last_name', 'receiver_name', 'receiver_last_name']
