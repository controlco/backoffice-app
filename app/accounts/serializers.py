from rest_framework import serializers
from accounts.models import User
from property_manager.serializers import PropertySerializer


class UserSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "properties"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("HOLA")
        print(validated_data)
        user = User(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user
