from wagtail.snippets.models import register_snippet

from chat.models import Chat, Message

register_snippet(Chat)
register_snippet(Message)