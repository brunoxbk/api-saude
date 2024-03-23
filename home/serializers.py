from rest_framework import serializers
from .models import Category, PostPage
from wagtail.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "title",
            "file"
        ]


class CategorySerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "slug",
            "image"
        ]


class PostPageSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True)
    
    class Meta:
        model = PostPage
        fields = [
            "id",
            "title",
            "slug",
            "body",
            "categories",
            "owner"
        ]

