from rest_framework import serializers
from chat.models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'user', 'chat','created_at']


class ChatSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    class Meta:
        model = Chat
        fields = ['id', 'members', 'created_at', 'messages']