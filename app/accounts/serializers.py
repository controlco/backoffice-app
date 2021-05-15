from rest_framework import serializers
from accounts.models import User, Report
from property_manager.serializers import PropertySerializer
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


# class UserProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = UserProfile
#         fields = ('first_name', 'last_name', 'rut', 'birth_date')

class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('id', 'email','first_name', 'last_name', 'rut', 'birth_date', 'is_owner')

class UserRegistrationSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)
    #profile = UserSerializer(required=False)
    
    class Meta:
        model = User
        #fields = ('id', 'email', 'password', 'is_owner', 'is_active', 'is_superuser', 'profile', 'properties')
        fields = ('id', 'email', 'password', 'is_owner', 'is_active', 'is_superuser', 'first_name', 'last_name', 'rut', 'birth_date', 'properties')

        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        #profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        if user.is_owner == False:
            user.is_active = True
            user.save()
            
        # UserProfile.objects.create(
        #     user=user,
        #     first_name=profile_data['first_name'],
        #     last_name=profile_data['last_name'],
        #     rut=profile_data['rut'],
        #     birth_date=profile_data['birth_date'],
        # )
        return user


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exist'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ["title", "content", "owner", "reported_user"]


