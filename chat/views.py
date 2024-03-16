from chat.models import Chat
from chat.serializers import ChatListSerializer, ChatDetailSerializer
from rest_framework import generics


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatDetailSerializer