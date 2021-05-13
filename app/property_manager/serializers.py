from rest_framework import serializers
from accounts.models import User
from property_manager.models import Property, Region, District


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Property
        fields = ['title', 'owner', 'surface', 'adress',
                  'price', 'description', 'latitude', 'longitude']


class DistrictSerializer(serializers.ModelSerializer):
  #  property = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = District
        fields = ['name', 'region']


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['name', 'number']
