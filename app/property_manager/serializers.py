from rest_framework import serializers
from accounts.models import User
from property_manager.models import Property, Region, District


class DistrictSerializer(serializers.ModelSerializer):
  #  property = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['name', 'region', "id"]


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['name', 'number']


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    owner_id = serializers.ReadOnlyField(source='owner.id')
    district_name = serializers.ReadOnlyField(source='district.name')

    class Meta:
        model = Property
        fields = ['id', 'title', 'owner_id', 'owner', 'surface', 'adress',
                  'price', 'description', 'latitude', 'longitude', 'district',
                  'district_name', 'electricity_service', 'water_service']
