from chat.models import Chat
from chat.serializers import ChatListSerializer, ChatDetailSerializer
from rest_framework import generics
from rest_framework.response import Response


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatListSerializer

    def list(self, request):
        queryset = self.get_queryset().filter(members=request.user) 
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatDetailSerializer
