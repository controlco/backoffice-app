from rest_framework import serializers
from chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    from_user_first_name = serializers.ReadOnlyField(
        source='from_user.first_name')
    from_user_last_name = serializers.ReadOnlyField(
        source='from_user.last_name')
    to_user_first_name = serializers.ReadOnlyField(
        source='to_user.first_name')
    to_user_last_name = serializers.ReadOnlyField(
        source='to_user.last_name')
    from_user_email = serializers.ReadOnlyField(source='from_user.email')
    from_id = serializers.ReadOnlyField(source='from_user.id')
    to_user_email = serializers.ReadOnlyField(source='to_user.email')

    class Meta:
        model = Message
        fields = ["id", "subject", "content", "from_user_email",
                  "from_id", "to_user_email", "to_user", "read",
                  "from_user_first_name", "from_user_last_name",
                  "to_user_first_name", "to_user_last_name"]
