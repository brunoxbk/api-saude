from rest_framework import serializers
from chat.models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'user', 'chat','created_at']


class ChatListSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    slug = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Chat
        fields = ['id', 'members', 'messages', 'created_at', 'slug']

class ChatDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    slug = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = Chat
        fields = ['id', 'members', 'created_at', 'messages', 'slug']