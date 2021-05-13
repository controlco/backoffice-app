from rest_framework import serializers
from accounts.models import User, Report, UserProfile
from property_manager.serializers import PropertySerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'rut', 'birth_date')


class UserRegistrationSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)
    profile = UserSerializer(required=False)
    
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'profile', 'properties')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            rut=profile_data['rut'],
            birth_date=profile_data['birth_date'],
        )
        return user


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ["title", "content", "owner", "reported_user"]
