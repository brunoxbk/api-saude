
import os
import socketio
from chat.models import Chat, Message
from chat.serializers import ChatListSerializer, ChatDetailSerializer, MessageSerializer

async_mode = None


basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode)


# @sio.event
# def my_event(sid, message):
#     sio.emit('my_response', {'data': message['data']}, room=sid)


# @sio.event
# def my_broadcast_event(sid, message):
#     sio.emit('my_response', {'data': message['data']})


# @sio.event
# def join(sid, message):
#     sio.enter_room(sid, message['room'])
#     sio.emit('my_response', {'data': 'Entered room: ' + message['room']},
#              room=sid)


# @sio.event
# def leave(sid, message):
#     sio.leave_room(sid, message['room'])
#     sio.emit('my_response', {'data': 'Left room: ' + message['room']},
#              room=sid)


# @sio.event
# def close_room(sid, message):
#     sio.emit('my_response',
#              {'data': 'Room ' + message['room'] + ' is closing.'},
#              room=message['room'])
#     sio.close_room(message['room'])


# @sio.event
# def my_room_event(sid, message):
#     sio.emit('my_response', {'data': message['data']}, room=message['room'])


@sio.event
def disconnect_request(sid):
    sio.disconnect(sid)


@sio.event
def connect(sid, environ):
    sio.emit('my_response', {'data': 'Connected', 'count': 0}, room=sid)


@sio.event
def disconnect(sid):
    print('Client disconnected')

# novo
    
@sio.event
def create_room(sid, name):
    print('create teste', name)
    chat = Chat()
    # print(chat)
    chat.save()
    # print(chat)
    sio.enter_room(sid, chat.slug)
    chats = Chat.objects.all()
    sio.emit('rooms_list', ChatDetailSerializer(chats, many=True).data)


@sio.event
def find_room(sid, pk):
    print(sid)
    chat = Chat.objects.get(pk=pk)
    chat.save()
    messages = chat.messages.all()
    sio.emit('found_room', MessageSerializer(messages, many=True).data)

@sio.event
def new_message(sid, data):
    chat = Chat.objects.get(pk=data['room_id'])
    chat.save()

    print(data)

    message = Message(
        chat=chat,
        text=data['text'],
        user_id=data['user']['pk']
    )

    message.save()
    
    chats = Chat.objects.all()
    messages = chat.messages.all()

    sio.emit("room_message", MessageSerializer(message).data, room=sid)

    sio.emit('rooms_list', ChatDetailSerializer(chats, many=True).data)
    sio.emit('found_room', MessageSerializer(messages, many=True).data)

# socket.on("createRoom", (name) => {
#     socket.join(name);
#     chatRooms.unshift({ id: generateID(), name, messages: [] });
#     socket.emit("roomsList", chatRooms);
# });

# socket.on("findRoom", (id) => {
#     let result = chatRooms.filter((room) => room.id == id);
#     // console.log(chatRooms);
#     socket.emit("foundRoom", result[0].messages);
#     // console.log("Messages Form", result[0].messages);
# });

# socket.on("newMessage", (data) => {
#     const { room_id, message, user, timestamp } = data;
#     let result = chatRooms.filter((room) => room.id == room_id);
#     const newMessage = {
#         id: generateID(),
#         text: message,
#         user,
#         time: `${timestamp.hour}:${timestamp.mins}`,
#     };
#     console.log("New Message", newMessage);
#     socket.to(result[0].name).emit("roomMessage", newMessage);
#     result[0].messages.push(newMessage);

#     socket.emit("roomsList", chatRooms);
#     socket.emit("foundRoom", result[0].messages);
# });

# socket.on("disconnect", () => {
#     socket.disconnect();
#     console.log("🔥: A user disconnected");
# });