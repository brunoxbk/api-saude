from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chat import views

urlpatterns = [
    path('', views.ChatList.as_view()),
    path('<int:pk>/', views.ChatDetail.as_view()),
]