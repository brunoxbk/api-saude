from django.db import models
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel
# from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.models import RevisionMixin
from django.contrib.auth.models import User


# @register_snippet
class Chat(ClusterableModel):
    # ask = models.CharField("Pergunta", null=False, blank=False)
    created_at = models.DateTimeField(
        "Criado em", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        "Alterado em", editable=False, auto_now=True)
    members = ParentalManyToManyField(User, blank=True)
    panels = [
        InlinePanel("messages", label="messages"),
    ]

    

    class Meta:
        db_table = "chats"
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
        ordering = ['-created_at']

    def __str__(self):
        return f"Chat {self.pk}"


# @register_snippet
class Message(models.Model):
    chat = ParentalKey(Chat, on_delete=models.CASCADE, related_name='messages')
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(
        "Criado em", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        "Alterado em", editable=False, auto_now=True)

    user = models.ForeignKey(
        User,
        verbose_name="Usuário", on_delete=models.CASCADE)

    panels = [
        FieldPanel("text"),
        FieldPanel("user"),
    ]

    search_fields = [
        index.SearchField('text'),
        index.AutocompleteField('text'),
    ]

    def __str__(self):
        return self.text
