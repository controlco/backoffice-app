from rest_framework import serializers
from accounts.models import User
from property_manager.models import Property


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Property
        fields = ['title', 'owner']
