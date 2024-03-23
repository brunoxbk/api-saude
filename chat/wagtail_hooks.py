from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from chat.models import Chat, Message
from chat.serializers import ChatDetailSerializer, MessageSerializer
from wagtail import hooks
from chat.socket import sio

class ChatViewSet(SnippetViewSet):
    model = Chat
    icon = "user"
    list_display = ["slug", ]
    list_per_page = 50
    copy_view_enabled = False
    inspect_view_enabled = True
    admin_url_namespace = "member_views"
    add_to_admin_menu =True


register_snippet(ChatViewSet)

# register_snippet(Chat)
register_snippet(Message)


@hooks.register('after_create_snippet')
def block_snippet_created(request, instance):
    print('aqui after', isinstance(instance, Message))
    if isinstance(instance, Message):
        print('criou uma mensagem')

        chats = Chat.objects.all()
        messages = instance.chat.messages.all()

        # sio.emit("room_message", MessageSerializer(instance).data, room=sid)

        sio.emit('rooms_list', ChatDetailSerializer(chats, many=True).data)
        sio.emit('found_room', MessageSerializer(messages, many=True).data)
    if isinstance(instance, Chat):
        print('criou uma chat')


@hooks.register('after_edit_snippet')
def block_snippet_created(request, instance):
    print('aqui after', isinstance(instance, Message))
    if isinstance(instance, Message):
        print('editou uma mensagem')

        
    if isinstance(instance, Chat):
        print('editou uma chat')

        chats = Chat.objects.all()
        messages = instance.messages.all()

        # sio.emit("room_message", MessageSerializer(instance).data, room=sid)

        sio.emit('rooms_list', ChatDetailSerializer(chats, many=True).data)
        sio.emit('found_room', MessageSerializer(messages, many=True).data)
