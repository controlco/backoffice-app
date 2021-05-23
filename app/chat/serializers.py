from rest_framework import serializers
from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    from_user_email = serializers.ReadOnlyField(source='from_user.email')
    from_id = serializers.ReadOnlyField(source='from_user.id')
    to_user_email = serializers.ReadOnlyField(source='to_user.email')

    class Meta:
        model = Message
        fields = ["id", "subject", "content", "from_user_email",
                  "from_id", "to_user_email", "to_user", "read"]
