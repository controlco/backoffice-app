from django.shortcuts import render
from django.urls.conf import path
from rest_framework import viewsets
from chat.models import Message
from accounts.models import User
from chat.serializers import MessageSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from chat.permissions import IsSenderOrReceiver
from django.db.models import Q

# Create your views here.


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.filter(
            Q(to_user=self.kwargs["user_pk"]) | Q(from_user=self.kwargs["user_pk"]))
        queryset = queryset.filter(
            Q(to_user=self.request.user.id) | Q(from_user=self.request.user.id))
        return queryset

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = (IsSenderOrReceiver,)
        return [permission() for permission in permission_classes]

    @ action(methods=["PATCH"], detail=True, url_path="read")
    def update_read(self, request, user_pk, pk=None):
        m = Message.objects.get(pk=pk)
        if m.to_user.id != request.user.id:
            return Response(
                {"detail": "Only the receiver can update read status."},
                status=status.HTTP_403_FORBIDDEN,
            )
        if not all(["read" == k for k in request.data]) or not (request.data["read"] == True or request.data["read"] == False):
            return Response(
                {"detail": "Data must be \"read\" = true or \"read\" = false."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        m.read = request.data["read"]
        m.save()
        return Response(MessageSerializer(m).data)

    @ action(methods=["GET"], detail=False, url_path="sent")
    def messages_sent(self, request, user_pk, pk=None):
        if request.user.id != user_pk:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        user = User.objects.get(pk=user_pk)
        messages_sent = user.from_message.all()
        return Response([MessageSerializer(m).data for m in messages_sent])

    @ action(methods=["GET"], detail=False, url_path="received")
    def messages_received(self, request, user_pk, pk=None):
        if request.user.id != user_pk:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        user = User.objects.get(pk=user_pk)
        messages_received = user.to_message.all()
        return Response([MessageSerializer(m).data for m in messages_received])
