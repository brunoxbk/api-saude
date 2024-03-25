from django.http import JsonResponse
from rest_framework import viewsets
from .models import Category, PostPage
from .serializers import CategorySerializer, PostPageSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PostPage.objects.all()
    serializer_class = PostPageSerializer


def home(request):
    data = {"ok": "ok"}
    return JsonResponse(data)