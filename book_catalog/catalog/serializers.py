from rest_framework import serializers
from .models import Book


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ('title', 'published', 'author')


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(default='')
    author_id = serializers.IntegerField(default=None)
    # author потом поменять на CharField()
    published = serializers.DateField(default=None)
    created= serializers.DateTimeField(read_only=True)
    modified = serializers.DateTimeField(read_only=True)


