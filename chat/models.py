from django.db import models
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
# from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.models import RevisionMixin
from django.contrib.auth.models import User
from django_currentuser.db.models import CurrentUserField
from django import forms


# @register_snippet
class Chat(ClusterableModel):
    created_at = models.DateTimeField(
        "Criado em", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        "Alterado em", editable=False, auto_now=True)
    members = ParentalManyToManyField(User, blank=True, verbose_name="Membros")


    panels = [
        FieldPanel("members", widget=forms.CheckboxSelectMultiple, read_only=True),
        InlinePanel("messages", label="Mensagens", panels=[FieldPanel("text"), FieldPanel("user", read_only=True)]),
        # MultiFieldPanel(
        #     [
        #         FieldPanel("messages",)
        #     ],
        #     heading="Mensagens"
        # ),
    ]

    @property
    def slug(self):
        return f'chat-{self.id}'


    class Meta:
        db_table = "chats"
        verbose_name = "Chat"
        verbose_name_plural = "Chats"
        ordering = ['-created_at']

    def __str__(self):
        return f"Chat {self.pk}"


# @register_snippet
class Message(models.Model):
    chat = ParentalKey(Chat, on_delete=models.CASCADE, related_name='messages', verbose_name="Chat")
    text = models.CharField("Texto",max_length=255)

    created_at = models.DateTimeField(
        "Criado em", editable=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        "Alterado em", editable=False, auto_now=True)

    user = CurrentUserField(verbose_name="Usuário")

    panels = [
        FieldPanel("chat"),
        FieldPanel("text"),
    ]

    search_fields = [
        index.SearchField('text'),
        index.AutocompleteField('text'),
    ]

    def __str__(self):
        return self.text
